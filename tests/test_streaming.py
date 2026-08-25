# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py
# 来源   : test_streaming.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '流式接收。\n\n存在理由很具体：缝合一次要吐 6,000 token、跑 2-16 分钟，非流式期间连接上\n一个字节都不动，中转站的上游会掐断。实测第 3 章四次尝试三次死在这一步，\n而输出只有它一半的 writer 五十次几乎没失败。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '流式接收。\n\n存在理由很具体：缝合一次要吐 6,000 token、跑 2-16 分钟，非流式期间连接上\n一个字节都不动，中转站的上游会掐断。实测第 3 章四次尝试三次死在这一步，\n而输出只有它一半的 writer 五十次几乎没失败。\n',
    8: 'Usage',
    10: 'Block',
    12: 'Message',
    14: 'FakeStream',
    16: 'FakeMessages',
    18: 'FakeClient',
    22: 'Schema',
    24: 'TestStreaming',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Usage', 0): 'Usage',
    ('Block', 0): 'Block',
    ('Block', 1): 'text',
    ('Block', 2): '缝好的整章',
    ('Message', 0): 'Message',
    ('Message', 1): 'claude-opus-5',
    ('Message', 2): 'end_turn',
    ('FakeStream', 0): 'FakeStream',
    ('__exit__', 1): 'closed',
    ('FakeMessages', 0): 'FakeMessages',
    ('create', 0): 'create',
    ('create', 1): 'how',
    ('stream', 0): 'stream',
    ('stream', 1): 'how',
    ('stream', 2): 'kwargs',
    ('parse', 0): 'parse',
    ('parse', 1): 'how',
    ('FakeClient', 0): 'FakeClient',
    ('backend', 0): 'packyapi',
    ('backend', 1): 'anthropic',
    ('backend', 2): 'K',
    ('prompt', 0): '角色',
    ('prompt', 1): '设定',
    ('prompt', 2): '写',
    ('Schema', 0): 'Schema',
    ('Schema', 1): 'bool',
    ('Schema', 2): 'ok',
    ('TestStreaming', 0): 'TestStreaming',
    ('test_on_by_default', 0): 'claude-opus-5',
    ('test_on_by_default', 2): 'how',
    ('test_on_by_default', 3): 'stream',
    ('test_on_by_default', 4): 'py1',
    ('test_on_by_default', 5): 'py4',
    ('test_on_by_default', 6): 'assert %(py6)s',
    ('test_on_by_default', 7): 'py6',
    ('test_stream_is_closed', 0): '不关流会漏连接 —— 长跑 140 章时这是会攒起来的那种问题。',
    ('test_stream_is_closed', 1): 'claude-opus-5',
    ('test_stream_is_closed', 3): 'closed',
    ('test_stream_is_closed', 5): 'py0',
    ('test_stream_is_closed', 6): 'rec',
    ('test_stream_is_closed', 7): 'py2',
    ('test_stream_is_closed', 8): 'py4',
    ('test_stream_is_closed', 9): 'py6',
    ('test_stream_is_closed', 10): 'py9',
    ('test_stream_is_closed', 11): 'assert %(py11)s',
    ('test_stream_is_closed', 12): 'py11',
    ('test_usage_survives_streaming', 0): '成本核算与缓存命中率全靠 usage。流式拿不到它就等于账本作废。',
    ('test_usage_survives_streaming', 1): 'claude-opus-5',
    ('test_usage_survives_streaming', 3): 'py1',
    ('test_usage_survives_streaming', 4): 'py4',
    ('test_usage_survives_streaming', 5): 'assert %(py6)s',
    ('test_usage_survives_streaming', 6): 'py6',
    ('test_usage_survives_streaming', 8): '缝好的整章',
    ('test_usage_survives_streaming', 9): 'py0',
    ('test_usage_survives_streaming', 10): 'r',
    ('test_usage_survives_streaming', 11): 'py2',
    ('test_usage_survives_streaming', 12): 'py5',
    ('test_usage_survives_streaming', 13): 'assert %(py7)s',
    ('test_usage_survives_streaming', 14): 'py7',
    ('test_usage_survives_streaming', 15): 'end_turn',
    ('test_request_body_is_unchanged', 0): '流式只改接收方式。请求体变了就意味着缓存前缀也可能变。',
    ('test_request_body_is_unchanged', 1): 'claude-opus-5',
    ('test_request_body_is_unchanged', 3): 'kwargs',
    ('test_request_body_is_unchanged', 4): 'model',
    ('test_request_body_is_unchanged', 5): 'py1',
    ('test_request_body_is_unchanged', 6): 'py4',
    ('test_request_body_is_unchanged', 7): 'assert %(py6)s',
    ('test_request_body_is_unchanged', 8): 'py6',
    ('test_request_body_is_unchanged', 10): 'max_tokens',
    ('test_request_body_is_unchanged', 11): 'system',
    ('test_request_body_is_unchanged', 12): 'cache_control',
    ('test_request_body_is_unchanged', 13): 'type',
    ('test_request_body_is_unchanged', 14): 'ephemeral',
    ('test_can_be_turned_off', 0): '哪天渠道的 SSE 出问题，要能一行配置退回去。',
    ('test_can_be_turned_off', 3): 'claude-opus-5',
    ('test_can_be_turned_off', 5): 'how',
    ('test_can_be_turned_off', 6): 'create',
    ('test_can_be_turned_off', 7): 'py1',
    ('test_can_be_turned_off', 8): 'py4',
    ('test_can_be_turned_off', 9): 'assert %(py6)s',
    ('test_can_be_turned_off', 10): 'py6',
    ('test_structured_output_never_streams', 0): 'parse 要拿到完整 JSON 才能校验；这类调用输出也短，不是超时来源。',
    ('test_structured_output_never_streams', 1): 'claude-opus-5',
    ('test_structured_output_never_streams', 4): 'how',
    ('test_structured_output_never_streams', 5): 'parse',
    ('test_structured_output_never_streams', 6): 'py1',
    ('test_structured_output_never_streams', 7): 'py4',
    ('test_structured_output_never_streams', 8): 'assert %(py6)s',
    ('test_structured_output_never_streams', 9): 'py6',
    ('test_retry_still_wraps_the_stream', 0): '流式调用同样会撞上 403/422，重试层不能因为换了接收方式就失效。',
    ('test_retry_still_wraps_the_stream', 1): 'n',
    ('test_retry_still_wraps_the_stream', 3): 'Flaky',
    ('test_retry_still_wraps_the_stream', 5): 'Boom',
    ('test_retry_still_wraps_the_stream', 8): 'claude-opus-5',
    ('test_retry_still_wraps_the_stream', 10): '缝好的整章',
    ('test_retry_still_wraps_the_stream', 11): 'py3',
    ('test_retry_still_wraps_the_stream', 12): 'py6',
    ('test_retry_still_wraps_the_stream', 13): '%(py8)s',
    ('test_retry_still_wraps_the_stream', 14): 'py8',
    ('test_retry_still_wraps_the_stream', 15): 'py10',
    ('test_retry_still_wraps_the_stream', 16): 'r',
    ('test_retry_still_wraps_the_stream', 17): 'py12',
    ('test_retry_still_wraps_the_stream', 18): 'py15',
    ('test_retry_still_wraps_the_stream', 19): '%(py17)s',
    ('test_retry_still_wraps_the_stream', 20): 'py17',
    ('test_retry_still_wraps_the_stream', 21): 'assert %(py20)s',
    ('test_retry_still_wraps_the_stream', 22): 'py20',
    ('Flaky', 0): 'TestStreaming.test_retry_still_wraps_the_stream.<locals>.Flaky',
    ('stream', 0): 'n',
    ('Boom', 0): 'TestStreaming.test_retry_still_wraps_the_stream.<locals>.Boom',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
class Usage:
    'Usage'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  18           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Usage')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          18
    # |               STORE_NAME               3 (__firstlineno__)
    # |  19           LOAD_SMALL_INT          11
    # |               LOAD_SMALL_INT          22
    # |               SWAP                     2
    # |               STORE_NAME               4 (input_tokens)
    # |               STORE_NAME               5 (output_tokens)
    # |  20           LOAD_SMALL_INT          33
    # |               LOAD_SMALL_INT           0
    # |               SWAP                     2
    # |               STORE_NAME               6 (cache_read_input_tokens)
    # |               STORE_NAME               7 (cache_creation_input_tokens)
    # |               LOAD_CONST               1 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               2 (None)
    # |               RETURN_VALUE

class Block:
    'Block'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  23           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Block')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          23
    # |               STORE_NAME               3 (__firstlineno__)
    # |  24           LOAD_CONST               1 ('text')
    # |               LOAD_CONST               2 ('缝好的整章')
    # |               SWAP                     2
    # |               STORE_NAME               4 (type)
    # |               STORE_NAME               5 (text)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE

class Message:
    'Message'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  27           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Message')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          27
    # |               STORE_NAME               3 (__firstlineno__)
    # |  28           LOAD_NAME                4 (Block)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               BUILD_LIST               1
    # |               LOAD_NAME                5 (Usage)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               SWAP                     2
    # |               STORE_NAME               6 (content)
    # |               STORE_NAME               7 (usage)
    # |  29           LOAD_CONST               1 ('claude-opus-5')
    # |               LOAD_CONST               2 ('end_turn')
    # |               SWAP                     2
    # |               STORE_NAME               8 (model)
    # |               STORE_NAME               9 (stop_reason)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE

class FakeStream:
    'FakeStream'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  32           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeStream')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          32
    # |               STORE_NAME               3 (__firstlineno__)
    # |  33           LOAD_CONST               1 (<code object __init__ at 0x1034b26a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 33>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # |  34           LOAD_CONST               2 (<code object __enter__ at 0x107f2ded0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 34>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (__enter__)
    # |  35           LOAD_CONST               3 (<code object __exit__ at 0x103493030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 35>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (__exit__)
    # |  36           LOAD_CONST               4 (<code object get_final_message at 0x1034b12f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 36>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (get_final_message)
    # |               LOAD_CONST               5 (('recorder',))
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x1034b26a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 33>:
    # |  33           RESUME                   0
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (recorder, self)
    # |               STORE_ATTR               0 (recorder)
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __enter__ at 0x107f2ded0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 34>:
    # |  34           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (self)
    # |               RETURN_VALUE
    # | Disassembly of <code object __exit__ at 0x103493030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 35>:
    # |  35           RESUME                   0
    # |               LOAD_CONST               0 (True)
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (recorder)
    # |               LOAD_CONST               1 ('closed')
    # |               STORE_SUBSCR
    # |               LOAD_CONST               2 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object get_final_message at 0x1034b12f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 36>:
    # |  36           RESUME                   0
    # |               LOAD_GLOBAL              1 (Message + NULL)
    # |               CALL                     0
    # |               RETURN_VALUE

    def __init__(self, recorder):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  33           RESUME                   0
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (recorder, self)
        # |               STORE_ATTR               0 (recorder)
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

    def __enter__(self):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  34           RESUME                   0
        # |               LOAD_FAST_BORROW         0 (self)
        # |               RETURN_VALUE

    def __exit__(self, *a):
        'closed'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  35           RESUME                   0
        # |               LOAD_CONST               0 (True)
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (recorder)
        # |               LOAD_CONST               1 ('closed')
        # |               STORE_SUBSCR
        # |               LOAD_CONST               2 (None)
        # |               RETURN_VALUE

    def get_final_message(self):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  36           RESUME                   0
        # |               LOAD_GLOBAL              1 (Message + NULL)
        # |               CALL                     0
        # |               RETURN_VALUE


class FakeMessages:
    'FakeMessages'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  39           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeMessages')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          39
    # |               STORE_NAME               3 (__firstlineno__)
    # |  40           LOAD_CONST               1 (<code object __init__ at 0x1034b2c40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 40>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # |  41           LOAD_CONST               2 (<code object create at 0x103517ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 41>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (create)
    # |  44           LOAD_CONST               3 (<code object stream at 0x1034be830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 44>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (stream)
    # |  48           LOAD_CONST               4 (<code object parse at 0x107f30030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 48>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (parse)
    # |               LOAD_CONST               5 (('recorder',))
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x1034b2c40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 40>:
    # |  40           RESUME                   0
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (recorder, self)
    # |               STORE_ATTR               0 (recorder)
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object create at 0x103517ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 41>:
    # |  41           RESUME                   0
    # |  42           LOAD_CONST               0 ('create')
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (recorder)
    # |               LOAD_CONST               1 ('how')
    # |               STORE_SUBSCR
    # |  43           LOAD_GLOBAL              3 (Message + NULL)
    # |               CALL                     0
    # |               RETURN_VALUE
    # | Disassembly of <code object stream at 0x1034be830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 44>:
    # |  44           RESUME                   0
    # |  45           LOAD_CONST               0 ('stream')
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (recorder)
    # |               LOAD_CONST               1 ('how')
    # |               STORE_SUBSCR
    # |  46           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (kw, self)
    # |               LOAD_ATTR                0 (recorder)
    # |               LOAD_CONST               2 ('kwargs')
    # |               STORE_SUBSCR
    # |  47           LOAD_GLOBAL              3 (FakeStream + NULL)
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (recorder)
    # |               CALL                     1
    # |               RETURN_VALUE
    # | Disassembly of <code object parse at 0x107f30030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 48>:
    # |  48           RESUME                   0
    # |  49           LOAD_CONST               0 ('parse')
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (recorder)
    # |               LOAD_CONST               1 ('how')
    # |               STORE_SUBSCR
    # |  50           LOAD_GLOBAL              3 (Message + NULL)
    # |               CALL                     0
    # |               RETURN_VALUE

    def __init__(self, recorder):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  40           RESUME                   0
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (recorder, self)
        # |               STORE_ATTR               0 (recorder)
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

    def create(self, **kw):
        'create'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  41           RESUME                   0
        # |  42           LOAD_CONST               0 ('create')
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (recorder)
        # |               LOAD_CONST               1 ('how')
        # |               STORE_SUBSCR
        # |  43           LOAD_GLOBAL              3 (Message + NULL)
        # |               CALL                     0
        # |               RETURN_VALUE

    def stream(self, **kw):
        'stream'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  44           RESUME                   0
        # |  45           LOAD_CONST               0 ('stream')
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (recorder)
        # |               LOAD_CONST               1 ('how')
        # |               STORE_SUBSCR
        # |  46           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (kw, self)
        # |               LOAD_ATTR                0 (recorder)
        # |               LOAD_CONST               2 ('kwargs')
        # |               STORE_SUBSCR
        # |  47           LOAD_GLOBAL              3 (FakeStream + NULL)
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (recorder)
        # |               CALL                     1
        # |               RETURN_VALUE

    def parse(self, **kw):
        'parse'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  48           RESUME                   0
        # |  49           LOAD_CONST               0 ('parse')
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (recorder)
        # |               LOAD_CONST               1 ('how')
        # |               STORE_SUBSCR
        # |  50           LOAD_GLOBAL              3 (Message + NULL)
        # |               CALL                     0
        # |               RETURN_VALUE


class FakeClient:
    'FakeClient'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  53           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeClient')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          53
    # |               STORE_NAME               3 (__firstlineno__)
    # |  54           LOAD_CONST               1 (<code object __init__ at 0x103519430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 54>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # |               LOAD_CONST               2 (('messages',))
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x103519430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 54>:
    # |  54           RESUME                   0
    # |               LOAD_GLOBAL              1 (FakeMessages + NULL)
    # |               LOAD_FAST_BORROW         1 (recorder)
    # |               CALL                     1
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               1 (messages)
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

    def __init__(self, recorder):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  54           RESUME                   0
        # |               LOAD_GLOBAL              1 (FakeMessages + NULL)
        # |               LOAD_FAST_BORROW         1 (recorder)
        # |               CALL                     1
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               1 (messages)
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE


def backend(recorder, **cfg):
    'packyapi'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  57           RESUME                   0
    # |  58           LOAD_GLOBAL              1 (dict + NULL)
    # |               LOAD_CONST               0 ('packyapi')
    # |               LOAD_CONST               1 ('anthropic')
    # |               LOAD_CONST               2 ('K')
    # |               LOAD_CONST               3 (('name', 'kind', 'api_key_env'))
    # |               CALL_KW                  3
    # |               STORE_FAST               2 (base)
    # |  59           LOAD_FAST_BORROW         2 (base)
    # |               LOAD_ATTR                3 (update + NULL|self)
    # |               LOAD_FAST_BORROW         1 (cfg)
    # |               CALL                     1
    # |               POP_TOP
    # |  60           LOAD_GLOBAL              5 (AnthropicBackend + NULL)
    # |               LOAD_GLOBAL              7 (ProviderConfig + NULL)
    # |               LOAD_CONST               5 (())
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         2 (base)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               LOAD_GLOBAL              9 (FakeClient + NULL)
    # |               LOAD_FAST_BORROW         0 (recorder)
    # |               CALL                     1
    # |               LOAD_CONST               4 (('client',))
    # |               CALL_KW                  2
    # |               RETURN_VALUE

def prompt():
    '角色'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  63           RESUME                   0
    # |  64           LOAD_GLOBAL              1 (Prompt + NULL)
    # |               LOAD_CONST               0 ('角色')
    # |               LOAD_CONST               1 ('设定')
    # |               LOAD_CONST               2 ('写')
    # |               LOAD_CONST               3 (('system_core', 'bible', 'instruction'))
    # |               CALL_KW                  3
    # |               RETURN_VALUE

class Schema:
    'Schema'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  67           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Schema')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          67
    # |               STORE_NAME               3 (__firstlineno__)
    # |               SETUP_ANNOTATIONS
    # |  68           LOAD_CONST               1 ('bool')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               2 ('ok')
    # |               STORE_SUBSCR
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE

class TestStreaming:
    'TestStreaming'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  71           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStreaming')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          71
    # |               STORE_NAME               3 (__firstlineno__)
    # |  72           LOAD_CONST               1 (<code object test_on_by_default at 0x7c4ed5af80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 72>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_on_by_default)
    # |  77           LOAD_CONST               2 (<code object test_stream_is_closed at 0x7c4ee3c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 77>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_stream_is_closed)
    # |  83           LOAD_CONST               3 (<code object test_usage_survives_streaming at 0x7c4f0aea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 83>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_usage_survives_streaming)
    # |  91           LOAD_CONST               4 (<code object test_request_body_is_unchanged at 0x7c4f222300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 91>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_request_body_is_unchanged)
    # |  99           LOAD_CONST               5 (<code object test_can_be_turned_off at 0x7c4ed59400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 99>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_can_be_turned_off)
    # | 105           LOAD_CONST               6 (<code object test_structured_output_never_streams at 0x7c4ed59680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 105>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_structured_output_never_streams)
    # | 111           LOAD_CONST               7 (<code object test_retry_still_wraps_the_stream at 0x7c4ee29800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 111>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_retry_still_wraps_the_stream)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_on_by_default at 0x7c4ed5af80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 72>:
    # |  72           RESUME                   0
    # |  73           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # |  74           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               0 ('claude-opus-5')
    # |               LOAD_CONST               1 (12000)
    # |               CALL                     3
    # |               POP_TOP
    # |  75           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               2 ('how')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               3 ('stream')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               6 ('assert %(py6)s')
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_stream_is_closed at 0x7c4ee3c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 77>:
    # |  77           RESUME                   0
    # |  79           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # |  80           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               1 ('claude-opus-5')
    # |               LOAD_CONST               2 (12000)
    # |               CALL                     3
    # |               POP_TOP
    # |  81           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_ATTR                6 (get)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               3 ('closed')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               LOAD_CONST               4 (True)
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               IS_OP                    0 (is)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('is',))
    # |               LOAD_FAST_BORROW         6 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('rec')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('rec')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py9')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_CONST              11 ('assert %(py11)s')
    # |               LOAD_CONST              12 ('py11')
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format12)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert7, @py_assert8)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_usage_survives_streaming at 0x7c4f0aea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 83>:
    # |  83           RESUME                   0
    # |  85           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # |  86           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               1 ('claude-opus-5')
    # |               LOAD_CONST               2 (12000)
    # |               CALL                     3
    # |               STORE_FAST               2 (r)
    # |  87           LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR                6 (input_tokens)
    # |               LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR                8 (output_tokens)
    # |               LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR               10 (cache_read)
    # |               BUILD_TUPLE              3
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_CONST              16 ((11, 22, 33))
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |  88           LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR               22 (text)
    # |               STORE_FAST               8 (@py_assert1)
    # |               LOAD_CONST               8 ('缝好的整章')
    # |               STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              10 ('r')
    # |               LOAD_GLOBAL             24 (@py_builtins)
    # |               LOAD_ATTR               26 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               28 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST              10 ('r')
    # |       L4:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py5')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format6)
    # |               LOAD_CONST              13 ('assert %(py7)s')
    # |               LOAD_CONST              14 ('py7')
    # |               LOAD_FAST_BORROW        10 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L5:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   73 (@py_assert3, @py_assert4)
    # |  89           LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR               30 (stop_reason)
    # |               STORE_FAST               8 (@py_assert1)
    # |               LOAD_CONST              15 ('end_turn')
    # |               STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.stop_reason\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              10 ('r')
    # |               LOAD_GLOBAL             24 (@py_builtins)
    # |               LOAD_ATTR               26 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               28 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L7)
    # |               NOT_TAKEN
    # |       L6:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L8)
    # |       L7:     LOAD_CONST              10 ('r')
    # |       L8:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py5')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format6)
    # |               LOAD_CONST              13 ('assert %(py7)s')
    # |               LOAD_CONST              14 ('py7')
    # |               LOAD_FAST_BORROW        10 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   73 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_request_body_is_unchanged at 0x7c4f222300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 91>:
    # |  91           RESUME                   0
    # |  93           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # |  94           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               1 ('claude-opus-5')
    # |               LOAD_CONST               2 (12000)
    # |               CALL                     3
    # |               POP_TOP
    # |  95           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               3 ('kwargs')
    # |               BINARY_OP               26 ([])
    # |               LOAD_CONST               4 ('model')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               1 ('claude-opus-5')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               7 ('assert %(py6)s')
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |  96           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               3 ('kwargs')
    # |               BINARY_OP               26 ([])
    # |               LOAD_CONST              10 ('max_tokens')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               2 (12000)
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               7 ('assert %(py6)s')
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |  97           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               3 ('kwargs')
    # |               BINARY_OP               26 ([])
    # |               LOAD_CONST              11 ('system')
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               LOAD_CONST              12 ('cache_control')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST              13 ('type')
    # |               LOAD_CONST              14 ('ephemeral')
    # |               BUILD_MAP                1
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               7 ('assert %(py6)s')
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L3:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_can_be_turned_off at 0x7c4ed59400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 99>:
    # |  99           RESUME                   0
    # | 101           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # | 102           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               1 (False)
    # |               LOAD_CONST               2 (('stream',))
    # |               CALL_KW                  2
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               3 ('claude-opus-5')
    # |               LOAD_CONST               4 (12000)
    # |               CALL                     3
    # |               POP_TOP
    # | 103           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               5 ('how')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               6 ('create')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_structured_output_never_streams at 0x7c4ed59680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 105>:
    # | 105           RESUME                   0
    # | 107           BUILD_MAP                0
    # |               STORE_FAST               1 (rec)
    # | 108           LOAD_GLOBAL              1 (backend + NULL)
    # |               LOAD_FAST_BORROW         1 (rec)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (call + NULL|self)
    # |               LOAD_GLOBAL              5 (prompt + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               1 ('claude-opus-5')
    # |               LOAD_CONST               2 (4000)
    # |               LOAD_GLOBAL              6 (Schema)
    # |               LOAD_CONST               3 (('output_format',))
    # |               CALL_KW                  4
    # |               POP_TOP
    # | 109           LOAD_FAST_BORROW         1 (rec)
    # |               LOAD_CONST               4 ('how')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               5 ('parse')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               6 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               8 ('assert %(py6)s')
    # |               LOAD_CONST               9 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_retry_still_wraps_the_stream at 0x7c4ee29800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 111>:
    # |   --           MAKE_CELL               18 (Boom)
    # |                MAKE_CELL               19 (rec)
    # |  111           RESUME                   0
    # |  113           LOAD_CONST               1 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF             19 (rec)
    # |  115           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        18 (Boom)
    # |                LOAD_FAST_BORROW        19 (rec)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST               2 (<code object Flaky at 0x103519630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 115>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_CONST               3 ('Flaky')
    # |                LOAD_GLOBAL              0 (FakeMessages)
    # |                CALL                     3
    # |                STORE_FAST               1 (Flaky)
    # |  122           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_CONST               4 (<code object Boom at 0x1034b31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 122>)
    # |                MAKE_FUNCTION
    # |                LOAD_CONST               5 ('Boom')
    # |                LOAD_GLOBAL              2 (Exception)
    # |                CALL                     3
    # |                STORE_DEREF             18 (Boom)
    # |  125           LOAD_GLOBAL              5 (backend + NULL)
    # |                LOAD_DEREF              19 (rec)
    # |                LOAD_CONST               6 (422)
    # |                BUILD_LIST               1
    # |                LOAD_SMALL_INT           2
    # |                LOAD_SMALL_INT           0
    # |                LOAD_CONST               7 (('retry_on_status', 'max_retries', 'retry_max_wait'))
    # |                CALL_KW                  4
    # |                STORE_FAST               2 (b)
    # |  126           LOAD_FAST_BORROW         1 (Flaky)
    # |                PUSH_NULL
    # |                LOAD_DEREF              19 (rec)
    # |                CALL                     1
    # |                LOAD_FAST_BORROW         2 (b)
    # |                LOAD_ATTR                6 (_client)
    # |                STORE_ATTR               4 (messages)
    # |  127           LOAD_FAST_BORROW         2 (b)
    # |                LOAD_ATTR               11 (call + NULL|self)
    # |                LOAD_GLOBAL             13 (prompt + NULL)
    # |                CALL                     0
    # |                LOAD_CONST               8 ('claude-opus-5')
    # |                LOAD_CONST               9 (12000)
    # |                CALL                     3
    # |                STORE_FAST               3 (r)
    # |  128           BUILD_LIST               0
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_DEREF              19 (rec)
    # |                LOAD_CONST               1 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               5 (@py_assert2)
    # |                LOAD_SMALL_INT           2
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       20 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR               14 (text)
    # |                STORE_FAST               9 (@py_assert11)
    # |                LOAD_CONST              10 ('缝好的整章')
    # |                STORE_FAST_LOAD_FAST   169 (@py_assert14, @py_assert11)
    # |                LOAD_FAST_BORROW        10 (@py_assert14)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert13, @py_assert13)
    # |                STORE_FAST               8 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW         8 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       370 (to L6)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              24 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              25 (('%(py3)s == %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py3')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format7)
    # |                LOAD_CONST              13 ('%(py8)s')
    # |                LOAD_CONST              14 ('py8')
    # |                LOAD_FAST_BORROW        12 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   212 (@py_format9, @py_assert1)
    # |                LOAD_ATTR               23 (append + NULL|self)
    # |                LOAD_FAST_BORROW        13 (@py_format9)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      185 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              24 (('==',))
    # |                LOAD_FAST_CHECK         11 (@py_assert13)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py12)s\n{%(py12)s = %(py10)s.text\n} == %(py15)s',))
    # |                LOAD_FAST_CHECK          9 (@py_assert11)
    # |                LOAD_FAST_CHECK         10 (@py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              15 ('py10')
    # |                LOAD_CONST              16 ('r')
    # |                LOAD_GLOBAL             24 (@py_builtins)
    # |                LOAD_ATTR               26 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               28 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST              16 ('r')
    # |        L4:     LOAD_CONST              17 ('py12')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py15')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format16)
    # |                LOAD_CONST              19 ('%(py17)s')
    # |                LOAD_CONST              20 ('py17')
    # |                LOAD_FAST_BORROW        14 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   244 (@py_format18, @py_assert1)
    # |                LOAD_ATTR               23 (append + NULL|self)
    # |                LOAD_FAST_BORROW        15 (@py_format18)
    # |                CALL                     1
    # |                POP_TOP
    # |        L5:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format19)
    # |                LOAD_CONST              21 ('assert %(py20)s')
    # |                LOAD_CONST              22 ('py20')
    # |                LOAD_FAST_BORROW        16 (@py_format19)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format21)
    # |                LOAD_GLOBAL             33 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               34 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        17 (@py_format21)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L6:     LOAD_CONST              23 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  186 (@py_assert13, @py_assert14)
    # |                LOAD_CONST              23 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object Flaky at 0x103519630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 115>:
    # |   --           COPY_FREE_VARS           2
    # |                MAKE_CELL                0 (__class__)
    # |  115           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Flaky')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT         115
    # |                STORE_NAME               3 (__firstlineno__)
    # |  116           LOAD_FAST_BORROW         1 (Boom)
    # |                LOAD_FAST_BORROW         0 (__class__)
    # |                LOAD_FAST_BORROW         2 (rec)
    # |                BUILD_TUPLE              3
    # |                LOAD_CONST               1 (<code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_NAME               4 (stream)
    # |                LOAD_CONST               2 (())
    # |                STORE_NAME               5 (__static_attributes__)
    # |                LOAD_FAST_BORROW         0 (__class__)
    # |                COPY                     1
    # |                STORE_NAME               6 (__classcell__)
    # |                RETURN_VALUE
    # | Disassembly of <code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>:
    # |   --           COPY_FREE_VARS           3
    # |  116           RESUME                   0
    # |  117           LOAD_DEREF               4 (rec)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |  118           LOAD_DEREF               4 (rec)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                COMPARE_OP              88 (bool(==))
    # |                POP_JUMP_IF_FALSE        9 (to L1)
    # |                NOT_TAKEN
    # |  119           LOAD_DEREF               2 (Boom)
    # |                PUSH_NULL
    # |                LOAD_CONST               1 (422)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |  120   L1:     LOAD_GLOBAL              0 (super)
    # |                LOAD_DEREF               3 (__class__)
    # |                LOAD_FAST_BORROW         0 (self)
    # |                LOAD_SUPER_ATTR          4 (stream)
    # |                PUSH_NULL
    # |                LOAD_CONST               2 (())
    # |                BUILD_MAP                0
    # |                LOAD_FAST_BORROW         1 (kw)
    # |                DICT_MERGE               1
    # |                CALL_FUNCTION_EX
    # |                RETURN_VALUE
    # | Disassembly of <code object Boom at 0x1034b31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 122>:
    # | 122           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Boom')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         122
    # |               STORE_NAME               3 (__firstlineno__)
    # | 123           LOAD_CONST               1 (422)
    # |               STORE_NAME               4 (status_code)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE

    def test_on_by_default(self):
        'claude-opus-5'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  72           RESUME                   0
        # |  73           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # |  74           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               0 ('claude-opus-5')
        # |               LOAD_CONST               1 (12000)
        # |               CALL                     3
        # |               POP_TOP
        # |  75           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               2 ('how')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               3 ('stream')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               6 ('assert %(py6)s')
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_stream_is_closed(self):
        '不关流会漏连接 —— 长跑 140 章时这是会攒起来的那种问题。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  77           RESUME                   0
        # |  79           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # |  80           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               1 ('claude-opus-5')
        # |               LOAD_CONST               2 (12000)
        # |               CALL                     3
        # |               POP_TOP
        # |  81           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_ATTR                6 (get)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               3 ('closed')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               LOAD_CONST               4 (True)
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               IS_OP                    0 (is)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('is',))
        # |               LOAD_FAST_BORROW         6 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('rec')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('rec')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py9')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_CONST              11 ('assert %(py11)s')
        # |               LOAD_CONST              12 ('py11')
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format12)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert7, @py_assert8)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_usage_survives_streaming(self):
        '成本核算与缓存命中率全靠 usage。流式拿不到它就等于账本作废。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  83           RESUME                   0
        # |  85           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # |  86           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               1 ('claude-opus-5')
        # |               LOAD_CONST               2 (12000)
        # |               CALL                     3
        # |               STORE_FAST               2 (r)
        # |  87           LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR                6 (input_tokens)
        # |               LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR                8 (output_tokens)
        # |               LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR               10 (cache_read)
        # |               BUILD_TUPLE              3
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_CONST              16 ((11, 22, 33))
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |  88           LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR               22 (text)
        # |               STORE_FAST               8 (@py_assert1)
        # |               LOAD_CONST               8 ('缝好的整章')
        # |               STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              10 ('r')
        # |               LOAD_GLOBAL             24 (@py_builtins)
        # |               LOAD_ATTR               26 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               28 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST              10 ('r')
        # |       L4:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py5')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format6)
        # |               LOAD_CONST              13 ('assert %(py7)s')
        # |               LOAD_CONST              14 ('py7')
        # |               LOAD_FAST_BORROW        10 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L5:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   73 (@py_assert3, @py_assert4)
        # |  89           LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR               30 (stop_reason)
        # |               STORE_FAST               8 (@py_assert1)
        # |               LOAD_CONST              15 ('end_turn')
        # |               STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.stop_reason\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              10 ('r')
        # |               LOAD_GLOBAL             24 (@py_builtins)
        # |               LOAD_ATTR               26 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               28 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L7)
        # |               NOT_TAKEN
        # |       L6:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L8)
        # |       L7:     LOAD_CONST              10 ('r')
        # |       L8:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py5')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format6)
        # |               LOAD_CONST              13 ('assert %(py7)s')
        # |               LOAD_CONST              14 ('py7')
        # |               LOAD_FAST_BORROW        10 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   73 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_request_body_is_unchanged(self):
        '流式只改接收方式。请求体变了就意味着缓存前缀也可能变。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  91           RESUME                   0
        # |  93           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # |  94           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               1 ('claude-opus-5')
        # |               LOAD_CONST               2 (12000)
        # |               CALL                     3
        # |               POP_TOP
        # |  95           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               3 ('kwargs')
        # |               BINARY_OP               26 ([])
        # |               LOAD_CONST               4 ('model')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               1 ('claude-opus-5')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               7 ('assert %(py6)s')
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |  96           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               3 ('kwargs')
        # |               BINARY_OP               26 ([])
        # |               LOAD_CONST              10 ('max_tokens')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               2 (12000)
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               7 ('assert %(py6)s')
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |  97           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               3 ('kwargs')
        # |               BINARY_OP               26 ([])
        # |               LOAD_CONST              11 ('system')
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               LOAD_CONST              12 ('cache_control')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST              13 ('type')
        # |               LOAD_CONST              14 ('ephemeral')
        # |               BUILD_MAP                1
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               7 ('assert %(py6)s')
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L3:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_can_be_turned_off(self):
        '哪天渠道的 SSE 出问题，要能一行配置退回去。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  99           RESUME                   0
        # | 101           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # | 102           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               1 (False)
        # |               LOAD_CONST               2 (('stream',))
        # |               CALL_KW                  2
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               3 ('claude-opus-5')
        # |               LOAD_CONST               4 (12000)
        # |               CALL                     3
        # |               POP_TOP
        # | 103           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               5 ('how')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               6 ('create')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_structured_output_never_streams(self):
        'parse 要拿到完整 JSON 才能校验；这类调用输出也短，不是超时来源。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 105           RESUME                   0
        # | 107           BUILD_MAP                0
        # |               STORE_FAST               1 (rec)
        # | 108           LOAD_GLOBAL              1 (backend + NULL)
        # |               LOAD_FAST_BORROW         1 (rec)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (call + NULL|self)
        # |               LOAD_GLOBAL              5 (prompt + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               1 ('claude-opus-5')
        # |               LOAD_CONST               2 (4000)
        # |               LOAD_GLOBAL              6 (Schema)
        # |               LOAD_CONST               3 (('output_format',))
        # |               CALL_KW                  4
        # |               POP_TOP
        # | 109           LOAD_FAST_BORROW         1 (rec)
        # |               LOAD_CONST               4 ('how')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               5 ('parse')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               6 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               8 ('assert %(py6)s')
        # |               LOAD_CONST               9 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_retry_still_wraps_the_stream(self):
        '流式调用同样会撞上 403/422，重试层不能因为换了接收方式就失效。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               18 (Boom)
        # |                MAKE_CELL               19 (rec)
        # |  111           RESUME                   0
        # |  113           LOAD_CONST               1 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF             19 (rec)
        # |  115           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        18 (Boom)
        # |                LOAD_FAST_BORROW        19 (rec)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST               2 (<code object Flaky at 0x103519630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 115>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_CONST               3 ('Flaky')
        # |                LOAD_GLOBAL              0 (FakeMessages)
        # |                CALL                     3
        # |                STORE_FAST               1 (Flaky)
        # |  122           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_CONST               4 (<code object Boom at 0x1034b31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 122>)
        # |                MAKE_FUNCTION
        # |                LOAD_CONST               5 ('Boom')
        # |                LOAD_GLOBAL              2 (Exception)
        # |                CALL                     3
        # |                STORE_DEREF             18 (Boom)
        # |  125           LOAD_GLOBAL              5 (backend + NULL)
        # |                LOAD_DEREF              19 (rec)
        # |                LOAD_CONST               6 (422)
        # |                BUILD_LIST               1
        # |                LOAD_SMALL_INT           2
        # |                LOAD_SMALL_INT           0
        # |                LOAD_CONST               7 (('retry_on_status', 'max_retries', 'retry_max_wait'))
        # |                CALL_KW                  4
        # |                STORE_FAST               2 (b)
        # |  126           LOAD_FAST_BORROW         1 (Flaky)
        # |                PUSH_NULL
        # |                LOAD_DEREF              19 (rec)
        # |                CALL                     1
        # |                LOAD_FAST_BORROW         2 (b)
        # |                LOAD_ATTR                6 (_client)
        # |                STORE_ATTR               4 (messages)
        # |  127           LOAD_FAST_BORROW         2 (b)
        # |                LOAD_ATTR               11 (call + NULL|self)
        # |                LOAD_GLOBAL             13 (prompt + NULL)
        # |                CALL                     0
        # |                LOAD_CONST               8 ('claude-opus-5')
        # |                LOAD_CONST               9 (12000)
        # |                CALL                     3
        # |                STORE_FAST               3 (r)
        # |  128           BUILD_LIST               0
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_DEREF              19 (rec)
        # |                LOAD_CONST               1 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               5 (@py_assert2)
        # |                LOAD_SMALL_INT           2
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       20 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR               14 (text)
        # |                STORE_FAST               9 (@py_assert11)
        # |                LOAD_CONST              10 ('缝好的整章')
        # |                STORE_FAST_LOAD_FAST   169 (@py_assert14, @py_assert11)
        # |                LOAD_FAST_BORROW        10 (@py_assert14)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert13, @py_assert13)
        # |                STORE_FAST               8 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW         8 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       370 (to L6)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              24 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              25 (('%(py3)s == %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py3')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format7)
        # |                LOAD_CONST              13 ('%(py8)s')
        # |                LOAD_CONST              14 ('py8')
        # |                LOAD_FAST_BORROW        12 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   212 (@py_format9, @py_assert1)
        # |                LOAD_ATTR               23 (append + NULL|self)
        # |                LOAD_FAST_BORROW        13 (@py_format9)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      185 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              24 (('==',))
        # |                LOAD_FAST_CHECK         11 (@py_assert13)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py12)s\n{%(py12)s = %(py10)s.text\n} == %(py15)s',))
        # |                LOAD_FAST_CHECK          9 (@py_assert11)
        # |                LOAD_FAST_CHECK         10 (@py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              15 ('py10')
        # |                LOAD_CONST              16 ('r')
        # |                LOAD_GLOBAL             24 (@py_builtins)
        # |                LOAD_ATTR               26 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               28 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST              16 ('r')
        # |        L4:     LOAD_CONST              17 ('py12')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert11)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py15')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format16)
        # |                LOAD_CONST              19 ('%(py17)s')
        # |                LOAD_CONST              20 ('py17')
        # |                LOAD_FAST_BORROW        14 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   244 (@py_format18, @py_assert1)
        # |                LOAD_ATTR               23 (append + NULL|self)
        # |                LOAD_FAST_BORROW        15 (@py_format18)
        # |                CALL                     1
        # |                POP_TOP
        # |        L5:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format19)
        # |                LOAD_CONST              21 ('assert %(py20)s')
        # |                LOAD_CONST              22 ('py20')
        # |                LOAD_FAST_BORROW        16 (@py_format19)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format21)
        # |                LOAD_GLOBAL             33 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               34 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        17 (@py_format21)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L6:     LOAD_CONST              23 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  186 (@py_assert13, @py_assert14)
        # |                LOAD_CONST              23 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object Flaky at 0x103519630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 115>:
        # |   --           COPY_FREE_VARS           2
        # |                MAKE_CELL                0 (__class__)
        # |  115           RESUME                   0
        # |                LOAD_NAME                0 (__name__)
        # |                STORE_NAME               1 (__module__)
        # |                LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Flaky')
        # |                STORE_NAME               2 (__qualname__)
        # |                LOAD_SMALL_INT         115
        # |                STORE_NAME               3 (__firstlineno__)
        # |  116           LOAD_FAST_BORROW         1 (Boom)
        # |                LOAD_FAST_BORROW         0 (__class__)
        # |                LOAD_FAST_BORROW         2 (rec)
        # |                BUILD_TUPLE              3
        # |                LOAD_CONST               1 (<code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_NAME               4 (stream)
        # |                LOAD_CONST               2 (())
        # |                STORE_NAME               5 (__static_attributes__)
        # |                LOAD_FAST_BORROW         0 (__class__)
        # |                COPY                     1
        # |                STORE_NAME               6 (__classcell__)
        # |                RETURN_VALUE
        # | Disassembly of <code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>:
        # |   --           COPY_FREE_VARS           3
        # |  116           RESUME                   0
        # |  117           LOAD_DEREF               4 (rec)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |  118           LOAD_DEREF               4 (rec)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                COMPARE_OP              88 (bool(==))
        # |                POP_JUMP_IF_FALSE        9 (to L1)
        # |                NOT_TAKEN
        # |  119           LOAD_DEREF               2 (Boom)
        # |                PUSH_NULL
        # |                LOAD_CONST               1 (422)
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |  120   L1:     LOAD_GLOBAL              0 (super)
        # |                LOAD_DEREF               3 (__class__)
        # |                LOAD_FAST_BORROW         0 (self)
        # |                LOAD_SUPER_ATTR          4 (stream)
        # |                PUSH_NULL
        # |                LOAD_CONST               2 (())
        # |                BUILD_MAP                0
        # |                LOAD_FAST_BORROW         1 (kw)
        # |                DICT_MERGE               1
        # |                CALL_FUNCTION_EX
        # |                RETURN_VALUE
        # | Disassembly of <code object Boom at 0x1034b31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 122>:
        # | 122           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Boom')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         122
        # |               STORE_NAME               3 (__firstlineno__)
        # | 123           LOAD_CONST               1 (422)
        # |               STORE_NAME               4 (status_code)
        # |               LOAD_CONST               2 (())
        # |               STORE_NAME               5 (__static_attributes__)
        # |               LOAD_CONST               3 (None)
        # |               RETURN_VALUE

        def Flaky():
            'TestStreaming.test_retry_still_wraps_the_stream.<locals>.Flaky'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           2
            # |                MAKE_CELL                0 (__class__)
            # |  115           RESUME                   0
            # |                LOAD_NAME                0 (__name__)
            # |                STORE_NAME               1 (__module__)
            # |                LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Flaky')
            # |                STORE_NAME               2 (__qualname__)
            # |                LOAD_SMALL_INT         115
            # |                STORE_NAME               3 (__firstlineno__)
            # |  116           LOAD_FAST_BORROW         1 (Boom)
            # |                LOAD_FAST_BORROW         0 (__class__)
            # |                LOAD_FAST_BORROW         2 (rec)
            # |                BUILD_TUPLE              3
            # |                LOAD_CONST               1 (<code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>)
            # |                MAKE_FUNCTION
            # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
            # |                STORE_NAME               4 (stream)
            # |                LOAD_CONST               2 (())
            # |                STORE_NAME               5 (__static_attributes__)
            # |                LOAD_FAST_BORROW         0 (__class__)
            # |                COPY                     1
            # |                STORE_NAME               6 (__classcell__)
            # |                RETURN_VALUE
            # | Disassembly of <code object stream at 0x1034d8960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_streaming.py", line 116>:
            # |   --           COPY_FREE_VARS           3
            # |  116           RESUME                   0
            # |  117           LOAD_DEREF               4 (rec)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |  118           LOAD_DEREF               4 (rec)
            # |                LOAD_CONST               0 ('n')
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                COMPARE_OP              88 (bool(==))
            # |                POP_JUMP_IF_FALSE        9 (to L1)
            # |                NOT_TAKEN
            # |  119           LOAD_DEREF               2 (Boom)
            # |                PUSH_NULL
            # |                LOAD_CONST               1 (422)
            # |                CALL                     1
            # |                RAISE_VARARGS            1
            # |  120   L1:     LOAD_GLOBAL              0 (super)
            # |                LOAD_DEREF               3 (__class__)
            # |                LOAD_FAST_BORROW         0 (self)
            # |                LOAD_SUPER_ATTR          4 (stream)
            # |                PUSH_NULL
            # |                LOAD_CONST               2 (())
            # |                BUILD_MAP                0
            # |                LOAD_FAST_BORROW         1 (kw)
            # |                DICT_MERGE               1
            # |                CALL_FUNCTION_EX
            # |                RETURN_VALUE

            def stream(self, **kw):
                'n'
                # ── 函数体（字节码重建见 BODY 段）──
                # |   --           COPY_FREE_VARS           3
                # |  116           RESUME                   0
                # |  117           LOAD_DEREF               4 (rec)
                # |                LOAD_CONST               0 ('n')
                # |                COPY                     2
                # |                COPY                     2
                # |                BINARY_OP               26 ([])
                # |                LOAD_SMALL_INT           1
                # |                BINARY_OP               13 (+=)
                # |                SWAP                     3
                # |                SWAP                     2
                # |                STORE_SUBSCR
                # |  118           LOAD_DEREF               4 (rec)
                # |                LOAD_CONST               0 ('n')
                # |                BINARY_OP               26 ([])
                # |                LOAD_SMALL_INT           1
                # |                COMPARE_OP              88 (bool(==))
                # |                POP_JUMP_IF_FALSE        9 (to L1)
                # |                NOT_TAKEN
                # |  119           LOAD_DEREF               2 (Boom)
                # |                PUSH_NULL
                # |                LOAD_CONST               1 (422)
                # |                CALL                     1
                # |                RAISE_VARARGS            1
                # |  120   L1:     LOAD_GLOBAL              0 (super)
                # |                LOAD_DEREF               3 (__class__)
                # |                LOAD_FAST_BORROW         0 (self)
                # |                LOAD_SUPER_ATTR          4 (stream)
                # |                PUSH_NULL
                # |                LOAD_CONST               2 (())
                # |                BUILD_MAP                0
                # |                LOAD_FAST_BORROW         1 (kw)
                # |                DICT_MERGE               1
                # |                CALL_FUNCTION_EX
                # |                RETURN_VALUE


        class Boom:
            'TestStreaming.test_retry_still_wraps_the_stream.<locals>.Boom'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 122           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestStreaming.test_retry_still_wraps_the_stream.<locals>.Boom')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         122
            # |               STORE_NAME               3 (__firstlineno__)
            # | 123           LOAD_CONST               1 (422)
            # |               STORE_NAME               4 (status_code)
            # |               LOAD_CONST               2 (())
            # |               STORE_NAME               5 (__static_attributes__)
            # |               LOAD_CONST               3 (None)
            # |               RETURN_VALUE


