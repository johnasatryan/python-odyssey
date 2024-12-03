import aiofiles
import json
import time
import asyncio
from errors import FileError


async def read_file_json(file_path: str):
  try:
    async with aiofiles.open(file_path, 'r') as file:
      content = await file.read()
      return json.loads(content) if content else []
  except FileNotFoundError:
    return []
  except Exception as e:
    raise FileError('File reading error:', e)   


async def write_file_json(file_path: str, data:list):
  try:
    async with  aiofiles.open(file_path, 'w') as file:
      await file.write(json.dumps(data, indent=2))
  except Exception as e:
    raise FileError('File reading error:', e)   
