from contextlib import asynccontextmanager
import asyncpg

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


class BasePsqlDTO():
    _HOST = DB_HOST
    _PORT = DB_PORT
    _DATABASE = DB_NAME
    _USER = DB_USER
    _PASSWORD =  DB_PASSWORD

    async def get_pool(self):
        pool = await asyncpg.create_pool(
            host=self._HOST,
            port=self._PORT,
            user=self._USER,
            password=self._PASSWORD,
            database=self._DATABASE,
            min_size=1,
            max_size=20,
        )

        await self._create_table(pool)  
        return pool
    
    @asynccontextmanager
    async def get_connection(self):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            yield conn
        await pool.close()

    async def _create_table(self, pool):
        """ 
        Creates recent_changes table 
        """
        
        async with pool.acquire() as conn:
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS recent_changes (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    title_url TEXT,
                    user_name VARCHAR(255),
                    edit_type VARCHAR(50),
                    comment TEXT,
                    language VARCHAR(255),
                    timestamp BIGINT
                )
                """
            )
