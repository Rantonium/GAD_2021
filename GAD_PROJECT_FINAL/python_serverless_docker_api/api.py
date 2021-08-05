from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/user_id={user_id}&script_id={script_id}&input_name={input_name}")
def run_script(user_id: int, script_id: str, input_name: str):
    run_container_cmd = subprocess.Popen("python run_docker.py " + str(user_id) + " " + str(script_id) + " " + str(input_name), stdout=subprocess.PIPE)
    result = run_container_cmd.communicate()[0]
    run_container_cmd.wait()
    str_result = str(result, "utf-8").replace("\r", "")
    if str_result.find("%%%%%"):
        print(str_result)
        str_result = str_result.split("%%%%%")[1]
    return {"result": str(str_result)}
