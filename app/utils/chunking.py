from typing import List
#defined 2 chunking strategy 

#fixed= splits text into chunks of a fixed size,by number of character,words,tokens
def fixed_chunk(text:str,size:int =500,overlap:int =50)-> List[str]:
    chunks=[]
    start=0

    while start <len(text):
        end=start+size
        chunks.append(text[start:end])
        start=end-overlap

    return chunks

#paragraph=splits text based on paragraph boundaries
def paragraph_chunk(text:str)->List[str]:
  return [p.strip() for p in text.split("\n\n") if p.strip()]