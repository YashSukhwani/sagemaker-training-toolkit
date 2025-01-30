# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: record.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 29, 3, "", "record.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0crecord.proto\x12\x0b\x61ialgs.data"H\n\rFloat32Tensor\x12\x12\n\x06values\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x10\n\x04keys\x18\x02 \x03(\x04\x42\x02\x10\x01\x12\x11\n\x05shape\x18\x03 \x03(\x04\x42\x02\x10\x01"H\n\rFloat64Tensor\x12\x12\n\x06values\x18\x01 \x03(\x01\x42\x02\x10\x01\x12\x10\n\x04keys\x18\x02 \x03(\x04\x42\x02\x10\x01\x12\x11\n\x05shape\x18\x03 \x03(\x04\x42\x02\x10\x01"F\n\x0bInt32Tensor\x12\x12\n\x06values\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x10\n\x04keys\x18\x02 \x03(\x04\x42\x02\x10\x01\x12\x11\n\x05shape\x18\x03 \x03(\x04\x42\x02\x10\x01",\n\x05\x42ytes\x12\r\n\x05value\x18\x01 \x03(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\t"\xd3\x01\n\x05Value\x12\x34\n\x0e\x66loat32_tensor\x18\x02 \x01(\x0b\x32\x1a.aialgs.data.Float32TensorH\x00\x12\x34\n\x0e\x66loat64_tensor\x18\x03 \x01(\x0b\x32\x1a.aialgs.data.Float64TensorH\x00\x12\x30\n\x0cint32_tensor\x18\x07 \x01(\x0b\x32\x18.aialgs.data.Int32TensorH\x00\x12#\n\x05\x62ytes\x18\t \x01(\x0b\x32\x12.aialgs.data.BytesH\x00\x42\x07\n\x05value"\xa9\x02\n\x06Record\x12\x33\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32!.aialgs.data.Record.FeaturesEntry\x12-\n\x05label\x18\x02 \x03(\x0b\x32\x1e.aialgs.data.Record.LabelEntry\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x15\n\rconfiguration\x18\x05 \x01(\t\x1a\x43\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.aialgs.data.Value:\x02\x38\x01\x1a@\n\nLabelEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.aialgs.data.Value:\x02\x38\x01\x42\x30\n com.amazonaws.aialgorithms.protoB\x0cRecordProtos'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "record_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n com.amazonaws.aialgorithms.protoB\014RecordProtos"
    _globals["_FLOAT32TENSOR"].fields_by_name["values"]._loaded_options = None
    _globals["_FLOAT32TENSOR"].fields_by_name["values"]._serialized_options = b"\020\001"
    _globals["_FLOAT32TENSOR"].fields_by_name["keys"]._loaded_options = None
    _globals["_FLOAT32TENSOR"].fields_by_name["keys"]._serialized_options = b"\020\001"
    _globals["_FLOAT32TENSOR"].fields_by_name["shape"]._loaded_options = None
    _globals["_FLOAT32TENSOR"].fields_by_name["shape"]._serialized_options = b"\020\001"
    _globals["_FLOAT64TENSOR"].fields_by_name["values"]._loaded_options = None
    _globals["_FLOAT64TENSOR"].fields_by_name["values"]._serialized_options = b"\020\001"
    _globals["_FLOAT64TENSOR"].fields_by_name["keys"]._loaded_options = None
    _globals["_FLOAT64TENSOR"].fields_by_name["keys"]._serialized_options = b"\020\001"
    _globals["_FLOAT64TENSOR"].fields_by_name["shape"]._loaded_options = None
    _globals["_FLOAT64TENSOR"].fields_by_name["shape"]._serialized_options = b"\020\001"
    _globals["_INT32TENSOR"].fields_by_name["values"]._loaded_options = None
    _globals["_INT32TENSOR"].fields_by_name["values"]._serialized_options = b"\020\001"
    _globals["_INT32TENSOR"].fields_by_name["keys"]._loaded_options = None
    _globals["_INT32TENSOR"].fields_by_name["keys"]._serialized_options = b"\020\001"
    _globals["_INT32TENSOR"].fields_by_name["shape"]._loaded_options = None
    _globals["_INT32TENSOR"].fields_by_name["shape"]._serialized_options = b"\020\001"
    _globals["_RECORD_FEATURESENTRY"]._loaded_options = None
    _globals["_RECORD_FEATURESENTRY"]._serialized_options = b"8\001"
    _globals["_RECORD_LABELENTRY"]._loaded_options = None
    _globals["_RECORD_LABELENTRY"]._serialized_options = b"8\001"
    _globals["_FLOAT32TENSOR"]._serialized_start = 29
    _globals["_FLOAT32TENSOR"]._serialized_end = 101
    _globals["_FLOAT64TENSOR"]._serialized_start = 103
    _globals["_FLOAT64TENSOR"]._serialized_end = 175
    _globals["_INT32TENSOR"]._serialized_start = 177
    _globals["_INT32TENSOR"]._serialized_end = 247
    _globals["_BYTES"]._serialized_start = 249
    _globals["_BYTES"]._serialized_end = 293
    _globals["_VALUE"]._serialized_start = 296
    _globals["_VALUE"]._serialized_end = 507
    _globals["_RECORD"]._serialized_start = 510
    _globals["_RECORD"]._serialized_end = 807
    _globals["_RECORD_FEATURESENTRY"]._serialized_start = 674
    _globals["_RECORD_FEATURESENTRY"]._serialized_end = 741
    _globals["_RECORD_LABELENTRY"]._serialized_start = 743
    _globals["_RECORD_LABELENTRY"]._serialized_end = 807
# @@protoc_insertion_point(module_scope)
