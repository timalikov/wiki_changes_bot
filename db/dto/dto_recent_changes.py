from db.base import BasePsqlDTO


class RecentChangesDTO(BasePsqlDTO):
    BASE_QUERY = "SELECT * FROM recent_changes"

    async def save_recent_change(self, data: dict):
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

    async def get_recent_changes(self, limit: int = 10):
        """
        Get the most recent changes
        """
        async with self.get_connection() as conn:
            rows = await conn.fetch(f"{self.BASE_QUERY} ORDER BY timestamp DESC LIMIT $1", limit)
            return [dict(row) for row in rows]