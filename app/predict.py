print(" * Starting predict.py...")

print(" * Loading imports...")
from werkzeug.utils import secure_filename
import sys, os, datetime, json, shutil, stat
from bioiain.machine.flows import predict


print(" * Copying FoldSeek...")
fs_path = "./tools/foldseek"
os.makedirs("./tools", exist_ok=True)
shutil.copy('/misc/foldseek', fs_path)

os.chmod(fs_path, stat.S_IRWXU )
print(" * Foldseek bin:", fs_path)
assert os.path.exists(fs_path)


JOBID = os.environ.get("JOBID", None)
print(" * JOBID:", JOBID)

def main():
    print(f" * Starting Job {JOBID} ...")

    in_folder = f"/predictions/in/{JOBID}"
    if not os.path.exists(in_folder):
        print("in_folder does not exist")
        return False
    try:
        info = json.load(open(f"{in_folder}/job_details.json", "r"))
    except FileNotFoundError:
        print("job_details.json does not exist")
        return False

    info["in_folder"] = in_folder


    out_folder = f"/predictions/out/{JOBID}"
    os.makedirs(out_folder, exist_ok=True)
    info["out_folder"] = out_folder

    info_file = os.path.join(out_folder, "job_details.json")
    info["info_file"] = info_file

    info ["status"] = "running"
    info["job_id"] = JOBID

    json.dump(info, open(info_file, "w"))

    fname = info["fname"]
    fpath = os.path.join(in_folder, fname)
    print("fpath:", fpath)
    assert os.path.exists(fpath)
    model_name = info["model_name"]
    model_path = os.path.join("/models", model_name)
    print("model_path: (data)", model_path)
    assert os.path.exists(model_path)

    chain = info.get("chain", "A")
    print("chain:", chain)


    try:
        job_info = predict(file_path=fpath, model_data_path=model_path, chain_id=chain, pred_folder=out_folder, use_temp=False, force=True, timestamp=JOBID, with_foldseek=False, foldseek_cmd="./foldseek", download_folder="/misc/predict/.models")
    except Exception as e:
        info["status"] = "failed"
        info["error"] = str(e)
        json.dump(info, open(info_file, "w"))
        return False

    info = info | job_info
    info["status"] = "ok"
    json.dump(info, open(info_file, "w"))

    print(f"Job {JOBID} completed!")
    return True




if __name__ == "__main__":
    print(" * Executing main() ...")
    success = main()
    print(f" * Execution complete! (success={success})")

