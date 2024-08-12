import asyncio

from src.database.manager import Database


async def main():
    # База данных
    db = Database()
    await db.create_new_tables()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Завершено пользователем")
    except Exception as e:
        print(e)
