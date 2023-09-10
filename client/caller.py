import asyncio, functools, time
import requests

base_url = "http://127.0.0.1"
port = "5000"


def response_print(response):
    try:
        print(response.json())
    except Exception:
        print(response.text)


endpoint_list = ["user", "bucket", "bucket_list", "object", "operation"]

# # ------------------------------------------------------------------------
# print("====================================================================")
# url = f"{base_url}:{port}/user"

# response = requests.get(f"{url}/jaijain")
# response_print(response)

# response = requests.put(f"{url}/jaijain", json={"name": "new jai"})
# response_print(response)

# response = requests.patch(f"{url}/jaijain", json={"name": "new jai"})
# response_print(response)

# response = requests.get(f"{url}/jaijain")
# response_print(response)

# response = requests.delete(f"{url}/jaijain")
# response_print(response)

# response = requests.get(f"{url}/jaijain")
# response_print(response)
# ------------------------------------------------------------------------
print("====================================================================")
url = f"{base_url}:{port}/bucket"

response = requests.put(f"{url}/bucket_0", json={"user_id": "jaijain"})
response_print(response)

response = requests.get(f"{url}/bucket_0", json={"user_id": "jaijain"})
response_print(response)

# response = requests.delete(f"{url}/bucket_0", json={"user_id": "jaijain"})
# response_print(response)

# response = requests.get(f"{url}/bucket_0", json={"user_id": "jaijain"})
# response_print(response)
# # ------------------------------------------------------------------------
# print("====================================================================")
# url = f"{base_url}:{port}/bucket_list"

# response = requests.get(url, json={"user_id": "jaijain"})
# response_print(response)
# ------------------------------------------------------------------------
print("====================================================================")
url = f"{base_url}:{port}"

response = requests.get(f"{url}/bucket_0/object_test_0", json={"user_id": "jaijain"})
response_print(response)

response = requests.put(
    f"{url}/bucket_0/object_test_0",
    json={
        "user_id": "jaijain",
        "repr": "this is going to be a binary representation of bucket_0/object_test_0 object",
    },
)
response_print(response)

response = requests.get(f"{url}/bucket_0/object_test_0", json={"user_id": "jaijain"})
response_print(response)

response = requests.patch(
    f"{url}/bucket_0/object_test_0",
    json={
        "user_id": "jaijain",
        "repr": "this is going to be a string representation of bucket_0/object_test_0 object",
    },
)
response_print(response)

response = requests.get(f"{url}/bucket_0/object_test_0", json={"user_id": "jaijain"})
response_print(response)

# response = requests.delete(
#     f"{url}/bucket_0/object_test_0",
#     json={
#         "user_id": "jaijain",
#     },
# )
# response_print(response)

# response = requests.get(f"{url}/bucket_0/object_test_0", json={"user_id": "jaijain"})
# response_print(response)
# ------------------------------------------------------------------------
print("====================================================================")
url = f"{base_url}:{port}"

response = requests.get(f"{url}/bucket_0/object_test_1", json={"user_id": "jaijain"})
response_print(response)

response = requests.put(
    f"{url}/bucket_0/object_test_1",
    json={
        "user_id": "jaijain",
        "repr": "this is object_test_1",
    },
)
response_print(response)

response = requests.get(f"{url}/bucket_0/object_test_1", json={"user_id": "jaijain"})
response_print(response)


# ------------------------------------------------------------------------
print("====================================================================")


def make_request(idx):
    print(f"call {idx}")
    start = time.perf_counter()
    response = requests.put(
        f"{url}/operation",
        json={
            "type": "copy",
            "params": {
                "source": "src object",
                "destination": "dest object",
            },
        },
    )
    end = time.perf_counter()
    response_print(response)
    print(f"time taken: {end - start} seconds")


def operation_method_sync():
    make_request()


async def operation_method_async():
    tasks = []
    for idx in range(1):
        task = asyncio.create_task(asyncio.to_thread(functools.partial(make_request, idx)))
        tasks.append(task)

    for task in tasks:
        await task


url = f"{base_url}:{port}"

# response = requests.get(f"{url}/bucket_0/object_test_1", json={"user_id": "jaijain"})
# response_print(response)

# start = time.perf_counter()
# response = requests.put(
#     f"{url}/operation",
#     json={
#         "type": "copy",
#         "params": {
#             "source": "src object",
#             "destination": "dest object",
#         },
#     },
# )
# end = time.perf_counter()
# response_print(response)
# print(f"time taken: {end - start} seconds")

# response = requests.get(f"{url}/bucket_0/object_test_1", json={"user_id": "jaijain"})
# response_print(response)

asyncio.run(operation_method_async())
