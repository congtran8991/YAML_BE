from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import text, select, update, delete

class DatabaseUtils():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_record(self, table_model, **kwargs):
        try:
            record_id = None
            record = table_model(**kwargs)  # Create an instance using keyword arguments
            # async with self.db_session.begin():  # This manage transaction automatically
            self.db_session.add(record)
            await self.db_session.flush() #you call flush(), changes are sent to the database. If not call this data is still in memory
            record_id = record.id
        except Exception as e:
            print(f"Error creating {table_model.__name__}: {e}")
        
        await self.db_session.commit()
        return record_id  # Return the created record
            
    
    async def update_record(self, sql_query):
        try:
            update_status = await self.db_session.execute(sql_query)
            if update_status.rowcount == 0:
                print("Failed to update record")
                update_status = False
            else:
                update_status = True
        except Exception as e:
            print(f"Error updating record: {e}")
            update_status = False
        
        await self.db_session.commit()
        return update_status
        
    async def delete_record(self, sql_query):
        try:
            remove_status = await self.db_session.execute(sql_query)
            if remove_status.rowcount == 0:
                print("Failed to delete record")
                remove_status = False
            else:
                remove_status = True
        except Exception as e:
            print(f"Error deleting record: {e}")
            remove_status = False

        await self.db_session.commit()
        return remove_status
        
    async def get_all_records(self, sql_query):
        result = await self.db_session.execute(sql_query)
        all_data = result.scalars().all()
        return all_data
    
    async def get_first_record(self, sql_query):
        result = await self.db_session.execute(sql_query)
        data = result.scalars().first()
        print(f"DDDDEEEBBUGGG GET data ={data}")
        return data
    
