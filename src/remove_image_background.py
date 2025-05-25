import replicate, os
from pathlib import Path

print(Path("/Users/justinbarry/Pictures/finetune-yt/06DE599B-23DD-4CE2-84FE-8BAF3126C465.jpg").as_posix())

token = input("Enter your API token: ")
os.environ["REPLICATE_API_TOKEN"] = token
replicate.Client(api_token=token)

input = {
    "image": Path("/Users/justinbarry/Pictures/finetune-yt/06DE599B-23DD-4CE2-84FE-8BAF3126C465.jpg").open("rb"),
}

output = replicate.run(
    "men1scus/birefnet:f74986db0355b58403ed20963af156525e2891ea3c2d499bfbfb2a28cd87c5d7",
    input=input
)
with open("../out/output_1.png", "wb") as file:
    file.write(output.read())
#=> output.png written to disk
