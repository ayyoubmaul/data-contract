#!/bin/bash

protoc --proto_path="proto_schema/" --python_out="plugins/table_schema/" $1

output=$(echo "$1" | cut -d '.' -f 1)

mv "plugins/table_schema/${output}_pb2.py" plugins/table_schema/$2
