from db.base import BasePsqlDTO


class UserLangDTO(BasePsqlDTO):
    BASE_QUERY = "SELECT * FROM user_lang"

    async def set_lang(self, user_id: int, lang: str) -> None:
        async with self.get_connection() as conn:
            await conn.execute(
                """
                INSERT INTO user_lang (user_id, lang)
                VALUES ($1, $2)
                """, 
                user_id, 
                lang
            )
    
    async def get_user_lang(self, user_id: int) -> str:
        async with self.get_connection() as conn:
            query = self.BASE_QUERY.replace("*", "lang") + "WHERE user_id = $1"
            lang = await conn.fetchval(query, user_id)
            return lang