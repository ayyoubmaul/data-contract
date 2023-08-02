def DataContract(proto_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func()
            [__validate(item, proto_func) for item in data]
        return wrapper
    return decorator

def __validate(item, proto_func):
    try:
        protobuf_data = proto_func(**item)
        protobuf_data.SerializeToString()

        return True
    except Exception as e:
        raise Exception(f'Validation failed for data: {item}, Error: {e}')
