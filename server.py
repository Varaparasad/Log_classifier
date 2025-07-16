import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException,File
from fastapi.responses import FileResponse
from classify import classify_all_logs

app=FastAPI()

@app.post('/classify')
async def classify_logs(file: UploadFile = File(...)):
    print("Received filename:", file.filename)
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400,detail="File must be a CSV")
    try:
        df=pd.read_csv(file.file)
        if 'source' not in df.columns or 'log_message' not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns")
        
        logs=list(zip(df['source'], df['log_message']))
        labels=classify_all_logs(logs)
        df['Label'] = labels

        output_file = './Resources/output.csv'
        df.to_csv(output_file, index=False)
        print("Classification completed successfully. File saved to output.csv")
        return FileResponse(output_file, media_type='text/csv', filename='output.csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()