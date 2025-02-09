from db.base import BasePsqlDTO


class RecentChangesDTO(BasePsqlDTO):
    BASE_QUERY = "SELECT * FROM recent_changes"

    async def save_recent_change(self, data: dict) -> None:
        async with self.get_connection() as conn:
            await conn.execute(
                """
                INSERT INTO recent_changes (title, title_url, user_name, edit_type, comment, language, timestamp)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                """,
                data.get("title", ""),
                data.get("title_url", ""),
                data.get("user_name", ""),
                data.get("edit_type", ""),
                data.get("comment", ""),
                data.get("language", "unknown"),
                data.get("timestamp", 0),
            )

    async def get_recent_changes(self, lang: str = None, limit: int = 10) -> list[dict]:
        """
        Get the most recent changes
        """
        async with self.get_connection() as conn:
            query = self.BASE_QUERY
            args = []

            if lang:
                query += " WHERE language = $1 "
                args.append(lang)

            query += f" ORDER BY timestamp DESC LIMIT ${len(args) + 1}"
            args.append(limit)

            rows = await conn.fetch(query, *args)
            return [dict(row) for row in rows]
        
    async def get_changes_count_by_date(self, date: str, lang: str = None) -> int:
        async with self.get_connection() as conn:
            query = self.BASE_QUERY.replace("*", "COUNT(*)") + " WHERE DATE(TO_TIMESTAMP(timestamp)) = $1"
            args = [date]

            if lang:
                query += f" AND language = ${len(args) + 1}"
                args.append(lang)

            result = await conn.fetchval(query, date, lang)
            return result if result else 0
            

