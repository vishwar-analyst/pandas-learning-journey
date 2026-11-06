import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players,columns=['player_id','name','age','position','team'])
    return list(df.shape)

    