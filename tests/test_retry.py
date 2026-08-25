# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py
# 来源   : test_retry.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '额外重试逻辑。\n\n存在理由很具体：aws-q 这类逆向渠道会间歇性返回 422，而 anthropic SDK\n只重试连接错误 / 408 / 409 / 429 / 5xx。缺这一层，自动跑 N 章撞一次就整轮中断。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '额外重试逻辑。\n\n存在理由很具体：aws-q 这类逆向渠道会间歇性返回 422，而 anthropic SDK\n只重试连接错误 / 408 / 409 / 429 / 5xx。缺这一层，自动跑 N 章撞一次就整轮中断。\n',
    6: 'Boom',
    8: 'Dummy',
    15: 'TestRetry',
    17: 'TestRetryObservability',
    19: 'ConnBoom',
    20: 'APIConnectionError',
    22: 'TestConnectionRetry',
    24: 'TestBackoffWindow',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Boom', 0): 'Boom',
    ('__annotate__', 1): 'status_code',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__init__', 0): 'HTTP ',
    ('Dummy', 0): 'Dummy',
    ('Dummy', 1): 'dummy',
    ('__annotate__', 1): 'prompt',
    ('__annotate__', 2): 'Prompt',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'Dummy',
    ('backend', 0): 't',
    ('backend', 1): 'dummy',
    ('backend', 2): 'K',
    ('no_sleep', 0): 'novel_agent.llm.backends.base.time.sleep',
    ('TestRetry', 0): 'TestRetry',
    ('test_succeeds_after_transient_422', 0): 'n',
    ('test_succeeds_after_transient_422', 2): 'ok',
    ('test_succeeds_after_transient_422', 3): 'py0',
    ('test_succeeds_after_transient_422', 4): 'backend',
    ('test_succeeds_after_transient_422', 5): 'py2',
    ('test_succeeds_after_transient_422', 6): 'py4',
    ('test_succeeds_after_transient_422', 7): 'py5',
    ('test_succeeds_after_transient_422', 8): 'send',
    ('test_succeeds_after_transient_422', 9): 'py7',
    ('test_succeeds_after_transient_422', 10): 'py10',
    ('test_succeeds_after_transient_422', 11): 'assert %(py12)s',
    ('test_succeeds_after_transient_422', 12): 'py12',
    ('test_succeeds_after_transient_422', 14): 'py1',
    ('test_succeeds_after_transient_422', 15): 'assert %(py6)s',
    ('test_succeeds_after_transient_422', 16): 'py6',
    ('send', 0): 'n',
    ('send', 2): 'ok',
    ('test_gives_up_after_max_retries', 0): 'n',
    ('test_gives_up_after_max_retries', 4): 'py1',
    ('test_gives_up_after_max_retries', 5): 'py4',
    ('test_gives_up_after_max_retries', 6): '应当是 1 次首发 + 3 次重试',
    ('test_gives_up_after_max_retries', 7): '\n>assert %(py6)s',
    ('test_gives_up_after_max_retries', 8): 'py6',
    ('send', 0): 'n',
    ('test_unlisted_status_raises_immediately', 0): '400 是请求本身有问题，重试没有意义，必须立刻失败。',
    ('test_unlisted_status_raises_immediately', 1): 'n',
    ('test_unlisted_status_raises_immediately', 4): 'py1',
    ('test_unlisted_status_raises_immediately', 5): 'py4',
    ('test_unlisted_status_raises_immediately', 6): 'assert %(py6)s',
    ('test_unlisted_status_raises_immediately', 7): 'py6',
    ('send', 0): 'n',
    ('test_no_retry_config_is_passthrough', 0): '主渠道没配额外重试时，不该有任何额外行为。',
    ('test_no_retry_config_is_passthrough', 1): 'n',
    ('test_no_retry_config_is_passthrough', 5): 'py1',
    ('test_no_retry_config_is_passthrough', 6): 'py4',
    ('test_no_retry_config_is_passthrough', 7): 'assert %(py6)s',
    ('test_no_retry_config_is_passthrough', 8): 'py6',
    ('send', 0): 'n',
    ('test_success_does_not_retry', 0): 'n',
    ('test_success_does_not_retry', 2): 'ok',
    ('test_success_does_not_retry', 3): 'py0',
    ('test_success_does_not_retry', 4): 'backend',
    ('test_success_does_not_retry', 5): 'py2',
    ('test_success_does_not_retry', 6): 'py4',
    ('test_success_does_not_retry', 7): 'py5',
    ('test_success_does_not_retry', 8): 'send',
    ('test_success_does_not_retry', 9): 'py7',
    ('test_success_does_not_retry', 10): 'py10',
    ('test_success_does_not_retry', 11): 'assert %(py12)s',
    ('test_success_does_not_retry', 12): 'py12',
    ('test_success_does_not_retry', 14): 'py1',
    ('test_success_does_not_retry', 15): 'assert %(py6)s',
    ('test_success_does_not_retry', 16): 'py6',
    ('send', 0): 'n',
    ('send', 1): 'ok',
    ('TestRetryObservability', 0): 'TestRetryObservability',
    ('TestRetryObservability', 1): '失败的尝试不记录就没法诊断吞吐 —— 实测遇到过成功 262s / 墙钟 2249s。',
    ('test_attempts_counted', 0): 'n',
    ('test_attempts_counted', 2): 'py0',
    ('test_attempts_counted', 3): 'b',
    ('test_attempts_counted', 4): 'py2',
    ('test_attempts_counted', 5): 'py5',
    ('test_attempts_counted', 6): 'assert %(py7)s',
    ('test_attempts_counted', 7): 'py7',
    ('send', 0): 'n',
    ('send', 2): 'ok',
    ('test_wait_accumulated', 3): 'py0',
    ('test_wait_accumulated', 4): 'b',
    ('test_wait_accumulated', 5): 'py2',
    ('test_wait_accumulated', 6): 'py5',
    ('test_wait_accumulated', 7): 'assert %(py7)s',
    ('test_wait_accumulated', 8): 'py7',
    ('test_stats_reset_between_calls', 2): 'py0',
    ('test_stats_reset_between_calls', 3): 'b',
    ('test_stats_reset_between_calls', 4): 'py2',
    ('test_stats_reset_between_calls', 5): 'py5',
    ('test_stats_reset_between_calls', 6): 'assert %(py7)s',
    ('test_stats_reset_between_calls', 7): 'py7',
    ('test_stats_reset_between_calls', 10): 'py4',
    ('test_stats_reset_between_calls', 11): '%(py9)s',
    ('test_stats_reset_between_calls', 12): 'py9',
    ('test_stats_reset_between_calls', 13): 'py11',
    ('test_stats_reset_between_calls', 14): 'py13',
    ('test_stats_reset_between_calls', 15): 'py16',
    ('test_stats_reset_between_calls', 16): '%(py18)s',
    ('test_stats_reset_between_calls', 17): 'py18',
    ('test_stats_reset_between_calls', 18): 'assert %(py21)s',
    ('test_stats_reset_between_calls', 19): 'py21',
    ('<lambda>', 0): 'ok',
    ('ConnBoom', 0): 'ConnBoom',
    ('ConnBoom', 1): '模拟 SDK 的连接异常（anthropic/openai 都叫 APIConnectionError）。',
    ('TestConnectionRetry', 0): 'TestConnectionRetry',
    ('TestConnectionRetry', 1): '断网期间整批任务失败过一次 —— SDK 自带重试次数太少，必须自己补。',
    ('test_connection_error_retried', 0): 'n',
    ('test_connection_error_retried', 3): 'ok',
    ('test_connection_error_retried', 4): 'py0',
    ('test_connection_error_retried', 5): 'backend',
    ('test_connection_error_retried', 6): 'py2',
    ('test_connection_error_retried', 7): 'py4',
    ('test_connection_error_retried', 8): 'py6',
    ('test_connection_error_retried', 9): 'py7',
    ('test_connection_error_retried', 10): 'send',
    ('test_connection_error_retried', 11): 'py9',
    ('test_connection_error_retried', 12): 'py12',
    ('test_connection_error_retried', 13): 'assert %(py14)s',
    ('test_connection_error_retried', 14): 'py14',
    ('test_connection_error_retried', 16): 'py1',
    ('test_connection_error_retried', 17): 'assert %(py6)s',
    ('send', 0): 'n',
    ('send', 1): 'Connection error.',
    ('send', 2): 'ok',
    ('test_timeout_retried', 1): 'ReadTimeout',
    ('test_timeout_retried', 2): 'n',
    ('test_timeout_retried', 5): 'ok',
    ('test_timeout_retried', 6): 'py0',
    ('test_timeout_retried', 7): 'backend',
    ('test_timeout_retried', 8): 'py2',
    ('test_timeout_retried', 9): 'py4',
    ('test_timeout_retried', 10): 'py6',
    ('test_timeout_retried', 11): 'py7',
    ('test_timeout_retried', 12): 'send',
    ('test_timeout_retried', 13): 'py9',
    ('test_timeout_retried', 14): 'py12',
    ('test_timeout_retried', 15): 'assert %(py14)s',
    ('test_timeout_retried', 16): 'py14',
    ('ReadTimeout', 0): 'TestConnectionRetry.test_timeout_retried.<locals>.ReadTimeout',
    ('send', 0): 'n',
    ('send', 1): 'timed out',
    ('send', 2): 'ok',
    ('test_can_be_disabled', 0): 'n',
    ('test_can_be_disabled', 5): 'py1',
    ('test_can_be_disabled', 6): 'py4',
    ('test_can_be_disabled', 7): 'assert %(py6)s',
    ('test_can_be_disabled', 8): 'py6',
    ('send', 0): 'n',
    ('send', 1): 'Connection error.',
    ('send', 0): 'something else',
    ('TestBackoffWindow', 0): 'TestBackoffWindow',
    ('TestBackoffWindow', 1): '号池的坏窗口是分钟级的。退避封顶太小，所有重试会落在同一个窗口里\n一起失败 —— 实测一次卷大纲就是这么挂的。',
    ('test_wait_respects_configured_cap', 0): 'novel_agent.llm.backends.base.time.sleep',
    ('test_wait_respects_configured_cap', 7): 'py0',
    ('test_wait_respects_configured_cap', 8): 'max',
    ('test_wait_respects_configured_cap', 9): 'py1',
    ('test_wait_respects_configured_cap', 10): 'waits',
    ('test_wait_respects_configured_cap', 11): 'py3',
    ('test_wait_respects_configured_cap', 12): 'py6',
    ('test_wait_respects_configured_cap', 13): '退避没有超过默认封顶，配置未生效',
    ('test_wait_respects_configured_cap', 14): '\n>assert %(py8)s',
    ('test_wait_respects_configured_cap', 15): 'py8',
    ('test_wait_respects_configured_cap', 16): 'sum',
    ('test_wait_respects_configured_cap', 17): '总重试窗口只有 ',
    ('test_wait_respects_configured_cap', 18): '.0f',
    ('test_wait_respects_configured_cap', 19): 's，跨不过分钟级抖动',
    ('test_default_cap_is_short', 0): '默认值保持小 —— 只有已知不稳的渠道才该配长窗口。',
    ('test_default_cap_is_short', 1): 'novel_agent.llm.backends.base.time.sleep',
    ('test_default_cap_is_short', 7): 'py0',
    ('test_default_cap_is_short', 8): 'max',
    ('test_default_cap_is_short', 9): 'py1',
    ('test_default_cap_is_short', 10): 'waits',
    ('test_default_cap_is_short', 11): 'py3',
    ('test_default_cap_is_short', 12): 'py6',
    ('test_default_cap_is_short', 13): 'assert %(py8)s',
    ('test_default_cap_is_short', 14): 'py8',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
class Boom:
    'Boom'
    # ── 函数体（字节码重建见 BODY 段）──
    # |   --           MAKE_CELL                0 (__class__)
    # |   15           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('Boom')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT          15
    # |                STORE_NAME               3 (__firstlineno__)
    # |   16           LOAD_CONST               1 (<code object __annotate__ at 0x103bc25b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 16>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW         0 (__class__)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               2 (<code object __init__ at 0x103c27dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 16>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |                STORE_NAME               4 (__init__)
    # |                LOAD_CONST               3 (('status_code',))
    # |                STORE_NAME               5 (__static_attributes__)
    # |                LOAD_FAST_BORROW         0 (__class__)
    # |                COPY                     1
    # |                STORE_NAME               6 (__classcell__)
    # |                RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x103bc25b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 16>:
    # |  16           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('status_code')
    # |               LOAD_CONST               2 ('int')
    # |               LOAD_CONST               3 ('return')
    # |               LOAD_CONST               4 ('None')
    # |               BUILD_MAP                2
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x103c27dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 16>:
    # |   --           COPY_FREE_VARS           1
    # |   16           RESUME                   0
    # |   17           LOAD_GLOBAL              0 (super)
    # |                LOAD_DEREF               2 (__class__)
    # |                LOAD_FAST_BORROW         0 (self)
    # |                LOAD_SUPER_ATTR          5 (__init__ + NULL|self)
    # |                LOAD_CONST               0 ('HTTP ')
    # |                LOAD_FAST_BORROW         1 (status_code)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                POP_TOP
    # |   18           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (status_code, self)
    # |                STORE_ATTR               2 (status_code)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE

    def __init__(self, status_code):
        'HTTP '
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           COPY_FREE_VARS           1
        # |   16           RESUME                   0
        # |   17           LOAD_GLOBAL              0 (super)
        # |                LOAD_DEREF               2 (__class__)
        # |                LOAD_FAST_BORROW         0 (self)
        # |                LOAD_SUPER_ATTR          5 (__init__ + NULL|self)
        # |                LOAD_CONST               0 ('HTTP ')
        # |                LOAD_FAST_BORROW         1 (status_code)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                POP_TOP
        # |   18           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (status_code, self)
        # |                STORE_ATTR               2 (status_code)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE


class Dummy:
    'Dummy'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  21           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Dummy')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          21
    # |               STORE_NAME               3 (__firstlineno__)
    # |  22           LOAD_CONST               1 ('dummy')
    # |               STORE_NAME               4 (kind)
    # |  24           LOAD_CONST               2 (<code object __annotate__ at 0x103bc26a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 24>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST               3 (<code object render at 0x103c79ed0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 24>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |               STORE_NAME               5 (render)
    # |  27           LOAD_CONST               7 ((None, None))
    # |               LOAD_CONST               5 (<code object call at 0x103bc12f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 27>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE   1 (defaults)
    # |               STORE_NAME               6 (call)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x103bc26a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 24>:
    # |  24           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('prompt')
    # |               LOAD_CONST               2 ('Prompt')
    # |               LOAD_CONST               3 ('return')
    # |               LOAD_CONST               4 ('dict')
    # |               BUILD_MAP                2
    # |               RETURN_VALUE
    # | Disassembly of <code object render at 0x103c79ed0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 24>:
    # |  24           RESUME                   0
    # |  25           BUILD_MAP                0
    # |               RETURN_VALUE
    # | Disassembly of <code object call at 0x103bc12f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 27>:
    # |  27           RESUME                   0
    # |  28           LOAD_GLOBAL              1 (RawResult + NULL)
    # |               LOAD_CONST               0 ('')
    # |               LOAD_FAST_BORROW         2 (model)
    # |               LOAD_CONST               1 (('text', 'model'))
    # |               CALL_KW                  2
    # |               RETURN_VALUE

    def render(self, prompt):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  24           RESUME                   0
        # |  25           BUILD_MAP                0
        # |               RETURN_VALUE

    def call(self, prompt, model, max_tokens, effort, output_format, **kw):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  27           RESUME                   0
        # |  28           LOAD_GLOBAL              1 (RawResult + NULL)
        # |               LOAD_CONST               0 ('')
        # |               LOAD_FAST_BORROW         2 (model)
        # |               LOAD_CONST               1 (('text', 'model'))
        # |               CALL_KW                  2
        # |               RETURN_VALUE


def backend(**kw):
    't'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  31           RESUME                   0
    # |  32           LOAD_GLOBAL              1 (dict + NULL)
    # |               LOAD_CONST               0 ('t')
    # |               LOAD_CONST               1 ('dummy')
    # |               LOAD_CONST               2 ('K')
    # |               LOAD_CONST               3 (422)
    # |               BUILD_LIST               1
    # |  33           LOAD_SMALL_INT           3
    # |  32           LOAD_CONST               4 (('name', 'kind', 'api_key_env', 'retry_on_status', 'max_retries'))
    # |               CALL_KW                  5
    # |               STORE_FAST               1 (base)
    # |  34           LOAD_FAST_BORROW         1 (base)
    # |               LOAD_ATTR                3 (update + NULL|self)
    # |               LOAD_FAST_BORROW         0 (kw)
    # |               CALL                     1
    # |               POP_TOP
    # |  35           LOAD_GLOBAL              5 (Dummy + NULL)
    # |               LOAD_GLOBAL              7 (ProviderConfig + NULL)
    # |               LOAD_CONST               5 (())
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         1 (base)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               CALL                     1
    # |               RETURN_VALUE

def no_sleep(monkeypatch):
    'novel_agent.llm.backends.base.time.sleep'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  38           RESUME                   0
    # |  40           LOAD_FAST_BORROW         0 (monkeypatch)
    # |               LOAD_ATTR                1 (setattr + NULL|self)
    # |               LOAD_CONST               0 ('novel_agent.llm.backends.base.time.sleep')
    # |               LOAD_CONST               1 (<code object <lambda> at 0x103c79df0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 40>)
    # |               MAKE_FUNCTION
    # |               CALL                     2
    # |               POP_TOP
    # |               LOAD_CONST               2 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x103c79df0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 40>:
    # |  40           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

class TestRetry:
    'TestRetry'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  43           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRetry')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          43
    # |               STORE_NAME               3 (__firstlineno__)
    # |  44           LOAD_CONST               1 (<code object test_succeeds_after_transient_422 at 0x74aedbd200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 44>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_succeeds_after_transient_422)
    # |  56           LOAD_CONST               2 (<code object test_gives_up_after_max_retries at 0x74af29f300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 56>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_gives_up_after_max_retries)
    # |  67           LOAD_CONST               3 (<code object test_unlisted_status_raises_immediately at 0x74af29f600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 67>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_unlisted_status_raises_immediately)
    # |  79           LOAD_CONST               4 (<code object test_no_retry_config_is_passthrough at 0x74af29f900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 79>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_no_retry_config_is_passthrough)
    # |  91           LOAD_CONST               5 (<code object test_success_does_not_retry at 0x74aedbd800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 91>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_success_does_not_retry)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_succeeds_after_transient_422 at 0x74aedbd200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 44>:
    # |   --           MAKE_CELL               13 (calls)
    # |   44           RESUME                   0
    # |   45           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF             13 (calls)
    # |   47           LOAD_FAST_BORROW        13 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103bce830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 47>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |   53           LOAD_GLOBAL              1 (backend + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR                2 (_retry)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                LOAD_CONST               2 ('ok')
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert8, @py_assert8)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       329 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py7)s\n{%(py7)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}._retry\n}(%(py5)s)\n} == %(py10)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert6, @py_assert9)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('backend')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('backend')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_CONST               8 ('send')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('send')
    # |        L6:     LOAD_CONST               9 ('py7')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py10')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format11)
    # |                LOAD_CONST              11 ('assert %(py12)s')
    # |                LOAD_CONST              12 ('py12')
    # |                LOAD_FAST_BORROW         7 (@py_format11)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert8, @py_assert9)
    # |   54           LOAD_DEREF              13 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               9 (@py_assert0)
    # |                LOAD_SMALL_INT           3
    # |                STORE_FAST_LOAD_FAST    57 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              14 ('py1')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format5)
    # |                LOAD_CONST              15 ('assert %(py6)s')
    # |                LOAD_CONST              16 ('py6')
    # |                LOAD_FAST_BORROW        11 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  163 (@py_assert2, @py_assert3)
    # |                LOAD_CONST              13 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object send at 0x103bce830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 47>:
    # |   --           COPY_FREE_VARS           1
    # |   47           RESUME                   0
    # |   48           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |   49           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           3
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE       12 (to L1)
    # |                NOT_TAKEN
    # |   50           LOAD_GLOBAL              1 (Boom + NULL)
    # |                LOAD_CONST               1 (422)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |   51   L1:     LOAD_CONST               2 ('ok')
    # |                RETURN_VALUE
    # | Disassembly of <code object test_gives_up_after_max_retries at 0x74af29f300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 56>:
    # |   --           MAKE_CELL                7 (calls)
    # |   56           RESUME                   0
    # |   57           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF              7 (calls)
    # |   59           LOAD_FAST_BORROW         7 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103bc6af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 59>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |   63           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (Boom)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   64           LOAD_GLOBAL              7 (backend + NULL)
    # |                LOAD_SMALL_INT           3
    # |                LOAD_CONST               2 (('max_retries',))
    # |                CALL_KW                  1
    # |                LOAD_ATTR                9 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |   63   L2:     LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |   65   L3:     LOAD_DEREF               7 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               2 (@py_assert0)
    # |                LOAD_SMALL_INT           4
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       148 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format5)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               6 ('应当是 1 次首发 + 3 次重试')
    # |                CALL                     1
    # |                LOAD_CONST               7 ('\n>assert %(py6)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_FAST_BORROW         5 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format7)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               3 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # |   63   L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 192 (to L3)
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object send at 0x103bc6af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 59>:
    # |   --           COPY_FREE_VARS           1
    # |   59           RESUME                   0
    # |   60           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |   61           LOAD_GLOBAL              1 (Boom + NULL)
    # |                LOAD_CONST               1 (422)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # | Disassembly of <code object test_unlisted_status_raises_immediately at 0x74af29f600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 67>:
    # |   --           MAKE_CELL                7 (calls)
    # |   67           RESUME                   0
    # |   69           LOAD_CONST               1 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF              7 (calls)
    # |   71           LOAD_FAST_BORROW         7 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               2 (<code object send at 0x103bc6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 71>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |   75           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (Boom)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   76           LOAD_GLOBAL              7 (backend + NULL)
    # |                CALL                     0
    # |                LOAD_ATTR                9 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |   75   L2:     LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |   77   L3:     LOAD_DEREF               7 (calls)
    # |                LOAD_CONST               1 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               2 (@py_assert0)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               8 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format5)
    # |                LOAD_CONST               6 ('assert %(py6)s')
    # |                LOAD_CONST               7 ('py6')
    # |                LOAD_FAST_BORROW         5 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               3 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # |   75   L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object send at 0x103bc6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 71>:
    # |   --           COPY_FREE_VARS           1
    # |   71           RESUME                   0
    # |   72           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |   73           LOAD_GLOBAL              1 (Boom + NULL)
    # |                LOAD_CONST               1 (400)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # | Disassembly of <code object test_no_retry_config_is_passthrough at 0x74af29f900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 79>:
    # |   --           MAKE_CELL                7 (calls)
    # |   79           RESUME                   0
    # |   81           LOAD_CONST               1 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF              7 (calls)
    # |   83           LOAD_FAST_BORROW         7 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               2 (<code object send at 0x103bc6d30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 83>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |   87           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (Boom)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   88           LOAD_GLOBAL              7 (backend + NULL)
    # |                BUILD_LIST               0
    # |                LOAD_CONST               3 (('retry_on_status',))
    # |                CALL_KW                  1
    # |                LOAD_ATTR                9 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |   87   L2:     LOAD_CONST               4 (None)
    # |                LOAD_CONST               4 (None)
    # |                LOAD_CONST               4 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |   89   L3:     LOAD_DEREF               7 (calls)
    # |                LOAD_CONST               1 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               2 (@py_assert0)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format5)
    # |                LOAD_CONST               7 ('assert %(py6)s')
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_FAST_BORROW         5 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               4 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               4 (None)
    # |                RETURN_VALUE
    # |   87   L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object send at 0x103bc6d30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 83>:
    # |   --           COPY_FREE_VARS           1
    # |   83           RESUME                   0
    # |   84           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |   85           LOAD_GLOBAL              1 (Boom + NULL)
    # |                LOAD_CONST               1 (422)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # | Disassembly of <code object test_success_does_not_retry at 0x74aedbd800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 91>:
    # |   --           MAKE_CELL               13 (calls)
    # |   91           RESUME                   0
    # |   92           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF             13 (calls)
    # |   94           LOAD_FAST_BORROW        13 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103c27ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 94>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |   98           LOAD_GLOBAL              1 (backend + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR                2 (_retry)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                LOAD_CONST               2 ('ok')
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert8, @py_assert8)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       329 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py7)s\n{%(py7)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}._retry\n}(%(py5)s)\n} == %(py10)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert6, @py_assert9)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('backend')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('backend')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_CONST               8 ('send')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('send')
    # |        L6:     LOAD_CONST               9 ('py7')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py10')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format11)
    # |                LOAD_CONST              11 ('assert %(py12)s')
    # |                LOAD_CONST              12 ('py12')
    # |                LOAD_FAST_BORROW         7 (@py_format11)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert8, @py_assert9)
    # |   99           LOAD_DEREF              13 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               9 (@py_assert0)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST    57 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              14 ('py1')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format5)
    # |                LOAD_CONST              15 ('assert %(py6)s')
    # |                LOAD_CONST              16 ('py6')
    # |                LOAD_FAST_BORROW        11 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  163 (@py_assert2, @py_assert3)
    # |                LOAD_CONST              13 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object send at 0x103c27ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 94>:
    # |   --           COPY_FREE_VARS           1
    # |   94           RESUME                   0
    # |   95           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |   96           LOAD_CONST               1 ('ok')
    # |                RETURN_VALUE

    def test_succeeds_after_transient_422(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               13 (calls)
        # |   44           RESUME                   0
        # |   45           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF             13 (calls)
        # |   47           LOAD_FAST_BORROW        13 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103bce830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 47>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |   53           LOAD_GLOBAL              1 (backend + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR                2 (_retry)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                LOAD_CONST               2 ('ok')
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert8, @py_assert8)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       329 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py7)s\n{%(py7)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}._retry\n}(%(py5)s)\n} == %(py10)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert6, @py_assert9)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('backend')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('backend')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_CONST               8 ('send')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('send')
        # |        L6:     LOAD_CONST               9 ('py7')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py10')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format11)
        # |                LOAD_CONST              11 ('assert %(py12)s')
        # |                LOAD_CONST              12 ('py12')
        # |                LOAD_FAST_BORROW         7 (@py_format11)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert8, @py_assert9)
        # |   54           LOAD_DEREF              13 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               9 (@py_assert0)
        # |                LOAD_SMALL_INT           3
        # |                STORE_FAST_LOAD_FAST    57 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              14 ('py1')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format5)
        # |                LOAD_CONST              15 ('assert %(py6)s')
        # |                LOAD_CONST              16 ('py6')
        # |                LOAD_FAST_BORROW        11 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  163 (@py_assert2, @py_assert3)
        # |                LOAD_CONST              13 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object send at 0x103bce830, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 47>:
        # |   --           COPY_FREE_VARS           1
        # |   47           RESUME                   0
        # |   48           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |   49           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           3
        # |                COMPARE_OP              18 (bool(<))
        # |                POP_JUMP_IF_FALSE       12 (to L1)
        # |                NOT_TAKEN
        # |   50           LOAD_GLOBAL              1 (Boom + NULL)
        # |                LOAD_CONST               1 (422)
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |   51   L1:     LOAD_CONST               2 ('ok')
        # |                RETURN_VALUE

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   47           RESUME                   0
            # |   48           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |   49           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           3
            # |                COMPARE_OP              18 (bool(<))
            # |                POP_JUMP_IF_FALSE       12 (to L1)
            # |                NOT_TAKEN
            # |   50           LOAD_GLOBAL              1 (Boom + NULL)
            # |                LOAD_CONST               1 (422)
            # |                CALL                     1
            # |                RAISE_VARARGS            1
            # |   51   L1:     LOAD_CONST               2 ('ok')
            # |                RETURN_VALUE


    def test_gives_up_after_max_retries(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                7 (calls)
        # |   56           RESUME                   0
        # |   57           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF              7 (calls)
        # |   59           LOAD_FAST_BORROW         7 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103bc6af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 59>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |   63           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (Boom)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   64           LOAD_GLOBAL              7 (backend + NULL)
        # |                LOAD_SMALL_INT           3
        # |                LOAD_CONST               2 (('max_retries',))
        # |                CALL_KW                  1
        # |                LOAD_ATTR                9 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |   63   L2:     LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |   65   L3:     LOAD_DEREF               7 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               2 (@py_assert0)
        # |                LOAD_SMALL_INT           4
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       148 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format5)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               6 ('应当是 1 次首发 + 3 次重试')
        # |                CALL                     1
        # |                LOAD_CONST               7 ('\n>assert %(py6)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_FAST_BORROW         5 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format7)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               3 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # |   63   L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 192 (to L3)
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti
        # | Disassembly of <code object send at 0x103bc6af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 59>:
        # |   --           COPY_FREE_VARS           1
        # |   59           RESUME                   0
        # |   60           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |   61           LOAD_GLOBAL              1 (Boom + NULL)
        # |                LOAD_CONST               1 (422)
        # |                CALL                     1
        # |                RAISE_VARARGS            1

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   59           RESUME                   0
            # |   60           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |   61           LOAD_GLOBAL              1 (Boom + NULL)
            # |                LOAD_CONST               1 (422)
            # |                CALL                     1
            # |                RAISE_VARARGS            1


    def test_unlisted_status_raises_immediately(self):
        '400 是请求本身有问题，重试没有意义，必须立刻失败。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                7 (calls)
        # |   67           RESUME                   0
        # |   69           LOAD_CONST               1 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF              7 (calls)
        # |   71           LOAD_FAST_BORROW         7 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               2 (<code object send at 0x103bc6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 71>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |   75           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (Boom)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   76           LOAD_GLOBAL              7 (backend + NULL)
        # |                CALL                     0
        # |                LOAD_ATTR                9 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |   75   L2:     LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |   77   L3:     LOAD_DEREF               7 (calls)
        # |                LOAD_CONST               1 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               2 (@py_assert0)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               8 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format5)
        # |                LOAD_CONST               6 ('assert %(py6)s')
        # |                LOAD_CONST               7 ('py6')
        # |                LOAD_FAST_BORROW         5 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               3 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # |   75   L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti
        # | Disassembly of <code object send at 0x103bc6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 71>:
        # |   --           COPY_FREE_VARS           1
        # |   71           RESUME                   0
        # |   72           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |   73           LOAD_GLOBAL              1 (Boom + NULL)
        # |                LOAD_CONST               1 (400)
        # |                CALL                     1
        # |                RAISE_VARARGS            1

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   71           RESUME                   0
            # |   72           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |   73           LOAD_GLOBAL              1 (Boom + NULL)
            # |                LOAD_CONST               1 (400)
            # |                CALL                     1
            # |                RAISE_VARARGS            1


    def test_no_retry_config_is_passthrough(self):
        '主渠道没配额外重试时，不该有任何额外行为。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                7 (calls)
        # |   79           RESUME                   0
        # |   81           LOAD_CONST               1 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF              7 (calls)
        # |   83           LOAD_FAST_BORROW         7 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               2 (<code object send at 0x103bc6d30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 83>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |   87           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (Boom)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   88           LOAD_GLOBAL              7 (backend + NULL)
        # |                BUILD_LIST               0
        # |                LOAD_CONST               3 (('retry_on_status',))
        # |                CALL_KW                  1
        # |                LOAD_ATTR                9 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |   87   L2:     LOAD_CONST               4 (None)
        # |                LOAD_CONST               4 (None)
        # |                LOAD_CONST               4 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |   89   L3:     LOAD_DEREF               7 (calls)
        # |                LOAD_CONST               1 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               2 (@py_assert0)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format5)
        # |                LOAD_CONST               7 ('assert %(py6)s')
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_FAST_BORROW         5 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               4 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               4 (None)
        # |                RETURN_VALUE
        # |   87   L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti
        # | Disassembly of <code object send at 0x103bc6d30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 83>:
        # |   --           COPY_FREE_VARS           1
        # |   83           RESUME                   0
        # |   84           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |   85           LOAD_GLOBAL              1 (Boom + NULL)
        # |                LOAD_CONST               1 (422)
        # |                CALL                     1
        # |                RAISE_VARARGS            1

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   83           RESUME                   0
            # |   84           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |   85           LOAD_GLOBAL              1 (Boom + NULL)
            # |                LOAD_CONST               1 (422)
            # |                CALL                     1
            # |                RAISE_VARARGS            1


    def test_success_does_not_retry(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               13 (calls)
        # |   91           RESUME                   0
        # |   92           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF             13 (calls)
        # |   94           LOAD_FAST_BORROW        13 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103c27ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 94>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |   98           LOAD_GLOBAL              1 (backend + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR                2 (_retry)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                LOAD_CONST               2 ('ok')
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert8, @py_assert8)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       329 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py7)s\n{%(py7)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}._retry\n}(%(py5)s)\n} == %(py10)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert6, @py_assert9)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('backend')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('backend')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_CONST               8 ('send')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('send')
        # |        L6:     LOAD_CONST               9 ('py7')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py10')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format11)
        # |                LOAD_CONST              11 ('assert %(py12)s')
        # |                LOAD_CONST              12 ('py12')
        # |                LOAD_FAST_BORROW         7 (@py_format11)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert8, @py_assert9)
        # |   99           LOAD_DEREF              13 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               9 (@py_assert0)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST    57 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              14 ('py1')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format5)
        # |                LOAD_CONST              15 ('assert %(py6)s')
        # |                LOAD_CONST              16 ('py6')
        # |                LOAD_FAST_BORROW        11 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  163 (@py_assert2, @py_assert3)
        # |                LOAD_CONST              13 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object send at 0x103c27ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 94>:
        # |   --           COPY_FREE_VARS           1
        # |   94           RESUME                   0
        # |   95           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |   96           LOAD_CONST               1 ('ok')
        # |                RETURN_VALUE

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   94           RESUME                   0
            # |   95           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |   96           LOAD_CONST               1 ('ok')
            # |                RETURN_VALUE



class TestRetryObservability:
    'TestRetryObservability'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 102           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRetryObservability')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         102
    # |               STORE_NAME               3 (__firstlineno__)
    # | 103           LOAD_CONST               1 ('失败的尝试不记录就没法诊断吞吐 —— 实测遇到过成功 262s / 墙钟 2249s。')
    # |               STORE_NAME               4 (__doc__)
    # | 105           LOAD_CONST               2 (<code object test_attempts_counted at 0x74af29fc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 105>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_attempts_counted)
    # | 118           LOAD_CONST               3 (<code object test_wait_accumulated at 0x74af294000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 118>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_wait_accumulated)
    # | 127           LOAD_CONST               4 (<code object test_stats_reset_between_calls at 0x74af077800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 127>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_stats_reset_between_calls)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_attempts_counted at 0x74af29fc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 105>:
    # |   --           MAKE_CELL                8 (calls)
    # |  105           RESUME                   0
    # |  106           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF              8 (calls)
    # |  108           LOAD_FAST_BORROW         8 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103bcefb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 108>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |  114           LOAD_GLOBAL              1 (backend + NULL)
    # |                CALL                     0
    # |                STORE_FAST               2 (b)
    # |  115           LOAD_FAST_BORROW         2 (b)
    # |                LOAD_ATTR                3 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |  116           LOAD_FAST_BORROW         2 (b)
    # |                LOAD_ATTR                4 (last_attempts)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_SMALL_INT           3
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              10 (('%(py2)s\n{%(py2)s = %(py0)s.last_attempts\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('b')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (b)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (b)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('b')
    # |        L3:     LOAD_CONST               4 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py5')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format6)
    # |                LOAD_CONST               6 ('assert %(py7)s')
    # |                LOAD_CONST               7 ('py7')
    # |                LOAD_FAST_BORROW         6 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format8)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |                LOAD_CONST               8 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object send at 0x103bcefb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 108>:
    # |   --           COPY_FREE_VARS           1
    # |  108           RESUME                   0
    # |  109           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |  110           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           3
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE       12 (to L1)
    # |                NOT_TAKEN
    # |  111           LOAD_GLOBAL              1 (Boom + NULL)
    # |                LOAD_CONST               1 (422)
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |  112   L1:     LOAD_CONST               2 ('ok')
    # |                RETURN_VALUE
    # | Disassembly of <code object test_wait_accumulated at 0x74af294000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 118>:
    # |  118            RESUME                   0
    # |  119            LOAD_CONST               0 (<code object send at 0x103bc24c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 119>)
    # |                 MAKE_FUNCTION
    # |                 STORE_FAST               1 (send)
    # |  122            LOAD_GLOBAL              1 (backend + NULL)
    # |                 LOAD_SMALL_INT           3
    # |                 LOAD_CONST               1 (('max_retries',))
    # |                 CALL_KW                  1
    # |                 STORE_FAST               2 (b)
    # |  123            LOAD_GLOBAL              2 (pytest)
    # |                 LOAD_ATTR                4 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (Boom)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |  124            LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR                9 (_retry + NULL|self)
    # |                 LOAD_FAST_BORROW         1 (send)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  123    L2:     LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  125    L3:     LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               10 (last_retry_wait)
    # |                 STORE_FAST               3 (@py_assert1)
    # |                 LOAD_SMALL_INT           0
    # |                 STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |                 LOAD_FAST_BORROW         4 (@py_assert4)
    # |                 COMPARE_OP             132 (>)
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       199 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               9 (('>',))
    # |                 LOAD_FAST_BORROW         5 (@py_assert3)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              10 (('%(py2)s\n{%(py2)s = %(py0)s.last_retry_wait\n} > %(py5)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               3 ('py0')
    # |                 LOAD_CONST               4 ('b')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               4 ('b')
    # |         L6:     LOAD_CONST               5 ('py2')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py5')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert4)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format6)
    # |                 LOAD_CONST               7 ('assert %(py7)s')
    # |                 LOAD_CONST               8 ('py7')
    # |                 LOAD_FAST_BORROW         6 (@py_format6)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format8)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format8)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               2 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |                 LOAD_CONST               2 (None)
    # |                 RETURN_VALUE
    # |  123    L8:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L9)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |         L9:     POP_TOP
    # |        L10:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 JUMP_BACKWARD_NO_INTERRUPT 246 (to L3)
    # |   --   L11:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L8 [2] lasti
    # |   L8 to L10 -> L11 [4] lasti
    # | Disassembly of <code object send at 0x103bc24c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 119>:
    # | 119           RESUME                   0
    # | 120           LOAD_GLOBAL              1 (Boom + NULL)
    # |               LOAD_CONST               0 (422)
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | Disassembly of <code object test_stats_reset_between_calls at 0x74af077800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 127>:
    # |  127            RESUME                   0
    # |  128            LOAD_GLOBAL              1 (backend + NULL)
    # |                 CALL                     0
    # |                 STORE_FAST               1 (b)
    # |  129            LOAD_GLOBAL              2 (pytest)
    # |                 LOAD_ATTR                4 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (Boom)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |  130            LOAD_FAST_BORROW         1 (b)
    # |                 LOAD_ATTR                9 (_retry + NULL|self)
    # |                 LOAD_CONST               0 (<code object <lambda> at 0x103bc6e50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>)
    # |                 MAKE_FUNCTION
    # |                 CALL                     1
    # |                 POP_TOP
    # |  129    L2:     LOAD_CONST               1 (None)
    # |                 LOAD_CONST               1 (None)
    # |                 LOAD_CONST               1 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  131    L3:     LOAD_FAST_BORROW         1 (b)
    # |                 LOAD_ATTR               10 (last_attempts)
    # |                 STORE_FAST               2 (@py_assert1)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
    # |                 LOAD_FAST_BORROW         3 (@py_assert4)
    # |                 COMPARE_OP             132 (>)
    # |                 STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       199 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              20 (('>',))
    # |                 LOAD_FAST_BORROW         4 (@py_assert3)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.last_attempts\n} > %(py5)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert1, @py_assert4)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py0')
    # |                 LOAD_CONST               3 ('b')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               3 ('b')
    # |         L6:     LOAD_CONST               4 ('py2')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               5 ('py5')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert4)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               5 (@py_format6)
    # |                 LOAD_CONST               6 ('assert %(py7)s')
    # |                 LOAD_CONST               7 ('py7')
    # |                 LOAD_FAST_BORROW         5 (@py_format6)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format8)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_format8)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               2 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   67 (@py_assert3, @py_assert4)
    # |  132            LOAD_FAST_BORROW         1 (b)
    # |                 LOAD_ATTR                9 (_retry + NULL|self)
    # |                 LOAD_CONST               8 (<code object <lambda> at 0x103c79d10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 132>)
    # |                 MAKE_FUNCTION
    # |                 CALL                     1
    # |                 POP_TOP
    # |  133            BUILD_LIST               0
    # |                 STORE_FAST_LOAD_FAST    33 (@py_assert1, b)
    # |                 LOAD_ATTR               10 (last_attempts)
    # |                 STORE_FAST               4 (@py_assert3)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST   116 (@py_assert6, @py_assert3)
    # |                 LOAD_FAST_BORROW         7 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
    # |                 STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       20 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 LOAD_ATTR               28 (last_retry_wait)
    # |                 STORE_FAST              10 (@py_assert12)
    # |                 LOAD_CONST               9 (0.0)
    # |                 STORE_FAST_LOAD_FAST   186 (@py_assert15, @py_assert12)
    # |                 LOAD_FAST_BORROW        11 (@py_assert15)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   204 (@py_assert14, @py_assert14)
    # |                 STORE_FAST               9 (@py_assert0)
    # |         L8:     LOAD_FAST_BORROW         9 (@py_assert0)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       448 (to L16)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              22 (('==',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              23 (('%(py4)s\n{%(py4)s = %(py2)s.last_attempts\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert3, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               4 ('py2')
    # |                 LOAD_CONST               3 ('b')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L9)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L10)
    # |                 NOT_TAKEN
    # |         L9:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L11)
    # |        L10:     LOAD_CONST               3 ('b')
    # |        L11:     LOAD_CONST              10 ('py4')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('py7')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format8)
    # |                 LOAD_CONST              11 ('%(py9)s')
    # |                 LOAD_CONST              12 ('py9')
    # |                 LOAD_FAST_BORROW         6 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST_LOAD_FAST   210 (@py_format10, @py_assert1)
    # |                 LOAD_ATTR               31 (append + NULL|self)
    # |                 LOAD_FAST_BORROW        13 (@py_format10)
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 LOAD_FAST_BORROW         8 (@py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE      185 (to L15)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              22 (('==',))
    # |                 LOAD_FAST_CHECK         12 (@py_assert14)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              24 (('%(py13)s\n{%(py13)s = %(py11)s.last_retry_wait\n} == %(py16)s',))
    # |                 LOAD_FAST_CHECK         10 (@py_assert12)
    # |                 LOAD_FAST_CHECK         11 (@py_assert15)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              13 ('py11')
    # |                 LOAD_CONST               3 ('b')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L12)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L13)
    # |                 NOT_TAKEN
    # |        L12:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (b)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L14)
    # |        L13:     LOAD_CONST               3 ('b')
    # |        L14:     LOAD_CONST              14 ('py13')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert12)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py16')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert15)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format17)
    # |                 LOAD_CONST              16 ('%(py18)s')
    # |                 LOAD_CONST              17 ('py18')
    # |                 LOAD_FAST_BORROW        14 (@py_format17)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST_LOAD_FAST   242 (@py_format19, @py_assert1)
    # |                 LOAD_ATTR               31 (append + NULL|self)
    # |                 LOAD_FAST_BORROW        15 (@py_format19)
    # |                 CALL                     1
    # |                 POP_TOP
    # |        L15:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_boolop)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (@py_assert1)
    # |                 LOAD_SMALL_INT           0
    # |                 CALL                     2
    # |                 BUILD_MAP                0
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              16 (@py_format20)
    # |                 LOAD_CONST              18 ('assert %(py21)s')
    # |                 LOAD_CONST              19 ('py21')
    # |                 LOAD_FAST_BORROW        16 (@py_format20)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              17 (@py_format22)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        17 (@py_format22)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L16:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               2 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert5)
    # |                 COPY                     1
    # |                 STORE_FAST               7 (@py_assert6)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert12)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  203 (@py_assert14, @py_assert15)
    # |                 LOAD_CONST               1 (None)
    # |                 RETURN_VALUE
    # |  129   L17:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L18)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L18:     POP_TOP
    # |        L19:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             3
    # |                 JUMP_BACKWARD_NO_INTERRUPT 782 (to L3)
    # |   --   L20:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L17 [2] lasti
    # |   L17 to L19 -> L20 [4] lasti
    # | Disassembly of <code object <lambda> at 0x103bc6e50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>:
    # | 130           RESUME                   0
    # |               LOAD_CONST               0 (<code object <genexpr> at 0x103c29430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST               2 (())
    # |               GET_ITER
    # |               CALL                     0
    # |               LOAD_ATTR                1 (throw + NULL|self)
    # |               LOAD_GLOBAL              3 (Boom + NULL)
    # |               LOAD_CONST               1 (422)
    # |               CALL                     1
    # |               CALL                     1
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103c29430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>:
    # |  130           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                 6 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (_, _)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD            8 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object <lambda> at 0x103c79d10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 132>:
    # | 132           RESUME                   0
    # |               LOAD_CONST               0 ('ok')
    # |               RETURN_VALUE

    def test_attempts_counted(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                8 (calls)
        # |  105           RESUME                   0
        # |  106           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF              8 (calls)
        # |  108           LOAD_FAST_BORROW         8 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103bcefb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 108>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |  114           LOAD_GLOBAL              1 (backend + NULL)
        # |                CALL                     0
        # |                STORE_FAST               2 (b)
        # |  115           LOAD_FAST_BORROW         2 (b)
        # |                LOAD_ATTR                3 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |  116           LOAD_FAST_BORROW         2 (b)
        # |                LOAD_ATTR                4 (last_attempts)
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_SMALL_INT           3
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 (('==',))
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              10 (('%(py2)s\n{%(py2)s = %(py0)s.last_attempts\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('b')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (b)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (b)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('b')
        # |        L3:     LOAD_CONST               4 ('py2')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py5')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format6)
        # |                LOAD_CONST               6 ('assert %(py7)s')
        # |                LOAD_CONST               7 ('py7')
        # |                LOAD_FAST_BORROW         6 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format8)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |                LOAD_CONST               8 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object send at 0x103bcefb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 108>:
        # |   --           COPY_FREE_VARS           1
        # |  108           RESUME                   0
        # |  109           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |  110           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           3
        # |                COMPARE_OP              18 (bool(<))
        # |                POP_JUMP_IF_FALSE       12 (to L1)
        # |                NOT_TAKEN
        # |  111           LOAD_GLOBAL              1 (Boom + NULL)
        # |                LOAD_CONST               1 (422)
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |  112   L1:     LOAD_CONST               2 ('ok')
        # |                RETURN_VALUE

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |  108           RESUME                   0
            # |  109           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |  110           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           3
            # |                COMPARE_OP              18 (bool(<))
            # |                POP_JUMP_IF_FALSE       12 (to L1)
            # |                NOT_TAKEN
            # |  111           LOAD_GLOBAL              1 (Boom + NULL)
            # |                LOAD_CONST               1 (422)
            # |                CALL                     1
            # |                RAISE_VARARGS            1
            # |  112   L1:     LOAD_CONST               2 ('ok')
            # |                RETURN_VALUE


    def test_wait_accumulated(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  118            RESUME                   0
        # |  119            LOAD_CONST               0 (<code object send at 0x103bc24c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 119>)
        # |                 MAKE_FUNCTION
        # |                 STORE_FAST               1 (send)
        # |  122            LOAD_GLOBAL              1 (backend + NULL)
        # |                 LOAD_SMALL_INT           3
        # |                 LOAD_CONST               1 (('max_retries',))
        # |                 CALL_KW                  1
        # |                 STORE_FAST               2 (b)
        # |  123            LOAD_GLOBAL              2 (pytest)
        # |                 LOAD_ATTR                4 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (Boom)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |  124            LOAD_FAST_BORROW         2 (b)
        # |                 LOAD_ATTR                9 (_retry + NULL|self)
        # |                 LOAD_FAST_BORROW         1 (send)
        # |                 CALL                     1
        # |                 POP_TOP
        # |  123    L2:     LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  125    L3:     LOAD_FAST_BORROW         2 (b)
        # |                 LOAD_ATTR               10 (last_retry_wait)
        # |                 STORE_FAST               3 (@py_assert1)
        # |                 LOAD_SMALL_INT           0
        # |                 STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |                 LOAD_FAST_BORROW         4 (@py_assert4)
        # |                 COMPARE_OP             132 (>)
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       199 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               9 (('>',))
        # |                 LOAD_FAST_BORROW         5 (@py_assert3)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              10 (('%(py2)s\n{%(py2)s = %(py0)s.last_retry_wait\n} > %(py5)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               3 ('py0')
        # |                 LOAD_CONST               4 ('b')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (b)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (b)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               4 ('b')
        # |         L6:     LOAD_CONST               5 ('py2')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py5')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert4)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format6)
        # |                 LOAD_CONST               7 ('assert %(py7)s')
        # |                 LOAD_CONST               8 ('py7')
        # |                 LOAD_FAST_BORROW         6 (@py_format6)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format8)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format8)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               2 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |                 LOAD_CONST               2 (None)
        # |                 RETURN_VALUE
        # |  123    L8:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L9)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |         L9:     POP_TOP
        # |        L10:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 JUMP_BACKWARD_NO_INTERRUPT 246 (to L3)
        # |   --   L11:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L8 [2] lasti
        # |   L8 to L10 -> L11 [4] lasti
        # | Disassembly of <code object send at 0x103bc24c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 119>:
        # | 119           RESUME                   0
        # | 120           LOAD_GLOBAL              1 (Boom + NULL)
        # |               LOAD_CONST               0 (422)
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def send():
            pass  # 无 docstring
            # ── 函数体（字节码重建见 BODY 段）──
            # | 119           RESUME                   0
            # | 120           LOAD_GLOBAL              1 (Boom + NULL)
            # |               LOAD_CONST               0 (422)
            # |               CALL                     1
            # |               RAISE_VARARGS            1


    def test_stats_reset_between_calls(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  127            RESUME                   0
        # |  128            LOAD_GLOBAL              1 (backend + NULL)
        # |                 CALL                     0
        # |                 STORE_FAST               1 (b)
        # |  129            LOAD_GLOBAL              2 (pytest)
        # |                 LOAD_ATTR                4 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (Boom)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |  130            LOAD_FAST_BORROW         1 (b)
        # |                 LOAD_ATTR                9 (_retry + NULL|self)
        # |                 LOAD_CONST               0 (<code object <lambda> at 0x103bc6e50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>)
        # |                 MAKE_FUNCTION
        # |                 CALL                     1
        # |                 POP_TOP
        # |  129    L2:     LOAD_CONST               1 (None)
        # |                 LOAD_CONST               1 (None)
        # |                 LOAD_CONST               1 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  131    L3:     LOAD_FAST_BORROW         1 (b)
        # |                 LOAD_ATTR               10 (last_attempts)
        # |                 STORE_FAST               2 (@py_assert1)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
        # |                 LOAD_FAST_BORROW         3 (@py_assert4)
        # |                 COMPARE_OP             132 (>)
        # |                 STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       199 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              20 (('>',))
        # |                 LOAD_FAST_BORROW         4 (@py_assert3)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.last_attempts\n} > %(py5)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert1, @py_assert4)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py0')
        # |                 LOAD_CONST               3 ('b')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               3 ('b')
        # |         L6:     LOAD_CONST               4 ('py2')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               5 ('py5')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert4)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               5 (@py_format6)
        # |                 LOAD_CONST               6 ('assert %(py7)s')
        # |                 LOAD_CONST               7 ('py7')
        # |                 LOAD_FAST_BORROW         5 (@py_format6)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format8)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_format8)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               2 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   67 (@py_assert3, @py_assert4)
        # |  132            LOAD_FAST_BORROW         1 (b)
        # |                 LOAD_ATTR                9 (_retry + NULL|self)
        # |                 LOAD_CONST               8 (<code object <lambda> at 0x103c79d10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 132>)
        # |                 MAKE_FUNCTION
        # |                 CALL                     1
        # |                 POP_TOP
        # |  133            BUILD_LIST               0
        # |                 STORE_FAST_LOAD_FAST    33 (@py_assert1, b)
        # |                 LOAD_ATTR               10 (last_attempts)
        # |                 STORE_FAST               4 (@py_assert3)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST   116 (@py_assert6, @py_assert3)
        # |                 LOAD_FAST_BORROW         7 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
        # |                 STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       20 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 LOAD_ATTR               28 (last_retry_wait)
        # |                 STORE_FAST              10 (@py_assert12)
        # |                 LOAD_CONST               9 (0.0)
        # |                 STORE_FAST_LOAD_FAST   186 (@py_assert15, @py_assert12)
        # |                 LOAD_FAST_BORROW        11 (@py_assert15)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   204 (@py_assert14, @py_assert14)
        # |                 STORE_FAST               9 (@py_assert0)
        # |         L8:     LOAD_FAST_BORROW         9 (@py_assert0)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       448 (to L16)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              22 (('==',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              23 (('%(py4)s\n{%(py4)s = %(py2)s.last_attempts\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert3, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               4 ('py2')
        # |                 LOAD_CONST               3 ('b')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L9)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L10)
        # |                 NOT_TAKEN
        # |         L9:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L11)
        # |        L10:     LOAD_CONST               3 ('b')
        # |        L11:     LOAD_CONST              10 ('py4')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('py7')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format8)
        # |                 LOAD_CONST              11 ('%(py9)s')
        # |                 LOAD_CONST              12 ('py9')
        # |                 LOAD_FAST_BORROW         6 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST_LOAD_FAST   210 (@py_format10, @py_assert1)
        # |                 LOAD_ATTR               31 (append + NULL|self)
        # |                 LOAD_FAST_BORROW        13 (@py_format10)
        # |                 CALL                     1
        # |                 POP_TOP
        # |                 LOAD_FAST_BORROW         8 (@py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE      185 (to L15)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              22 (('==',))
        # |                 LOAD_FAST_CHECK         12 (@py_assert14)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              24 (('%(py13)s\n{%(py13)s = %(py11)s.last_retry_wait\n} == %(py16)s',))
        # |                 LOAD_FAST_CHECK         10 (@py_assert12)
        # |                 LOAD_FAST_CHECK         11 (@py_assert15)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              13 ('py11')
        # |                 LOAD_CONST               3 ('b')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L12)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L13)
        # |                 NOT_TAKEN
        # |        L12:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (b)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L14)
        # |        L13:     LOAD_CONST               3 ('b')
        # |        L14:     LOAD_CONST              14 ('py13')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert12)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py16')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert15)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format17)
        # |                 LOAD_CONST              16 ('%(py18)s')
        # |                 LOAD_CONST              17 ('py18')
        # |                 LOAD_FAST_BORROW        14 (@py_format17)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST_LOAD_FAST   242 (@py_format19, @py_assert1)
        # |                 LOAD_ATTR               31 (append + NULL|self)
        # |                 LOAD_FAST_BORROW        15 (@py_format19)
        # |                 CALL                     1
        # |                 POP_TOP
        # |        L15:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_boolop)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (@py_assert1)
        # |                 LOAD_SMALL_INT           0
        # |                 CALL                     2
        # |                 BUILD_MAP                0
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              16 (@py_format20)
        # |                 LOAD_CONST              18 ('assert %(py21)s')
        # |                 LOAD_CONST              19 ('py21')
        # |                 LOAD_FAST_BORROW        16 (@py_format20)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              17 (@py_format22)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        17 (@py_format22)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L16:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               2 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert5)
        # |                 COPY                     1
        # |                 STORE_FAST               7 (@py_assert6)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert12)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  203 (@py_assert14, @py_assert15)
        # |                 LOAD_CONST               1 (None)
        # |                 RETURN_VALUE
        # |  129   L17:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L18)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L18:     POP_TOP
        # |        L19:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             3
        # |                 JUMP_BACKWARD_NO_INTERRUPT 782 (to L3)
        # |   --   L20:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L17 [2] lasti
        # |   L17 to L19 -> L20 [4] lasti
        # | Disassembly of <code object <lambda> at 0x103bc6e50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>:
        # | 130           RESUME                   0
        # |               LOAD_CONST               0 (<code object <genexpr> at 0x103c29430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>)
        # |               MAKE_FUNCTION
        # |               LOAD_CONST               2 (())
        # |               GET_ITER
        # |               CALL                     0
        # |               LOAD_ATTR                1 (throw + NULL|self)
        # |               LOAD_GLOBAL              3 (Boom + NULL)
        # |               LOAD_CONST               1 (422)
        # |               CALL                     1
        # |               CALL                     1
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103c29430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 130>:
        # |  130           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                 6 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (_, _)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD            8 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti
        # | Disassembly of <code object <lambda> at 0x103c79d10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 132>:
        # | 132           RESUME                   0
        # |               LOAD_CONST               0 ('ok')
        # |               RETURN_VALUE


class ConnBoom:
    'ConnBoom'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 136           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('ConnBoom')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         136
    # |               STORE_NAME               3 (__firstlineno__)
    # | 137           LOAD_CONST               1 ('模拟 SDK 的连接异常（anthropic/openai 都叫 APIConnectionError）。')
    # |               STORE_NAME               4 (__doc__)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE

class TestConnectionRetry:
    'TestConnectionRetry'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 143           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestConnectionRetry')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         143
    # |               STORE_NAME               3 (__firstlineno__)
    # | 144           LOAD_CONST               1 ('断网期间整批任务失败过一次 —— SDK 自带重试次数太少，必须自己补。')
    # |               STORE_NAME               4 (__doc__)
    # | 146           LOAD_CONST               2 (<code object test_connection_error_retried at 0x74aedbde00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 146>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_connection_error_retried)
    # | 158           LOAD_CONST               3 (<code object test_timeout_retried at 0x74af272d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 158>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_timeout_retried)
    # | 172           LOAD_CONST               4 (<code object test_can_be_disabled at 0x74af2a4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 172>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_can_be_disabled)
    # | 184           LOAD_CONST               5 (<code object test_non_connection_error_still_raises at 0x103c492f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 184>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_non_connection_error_still_raises)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_connection_error_retried at 0x74aedbde00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 146>:
    # |   --           MAKE_CELL               14 (calls)
    # |  146           RESUME                   0
    # |  147           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF             14 (calls)
    # |  149           LOAD_FAST_BORROW        14 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103bcf0f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 149>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |  155           BUILD_LIST               0
    # |                STORE_FAST               2 (@py_assert1)
    # |                LOAD_GLOBAL              1 (backend + NULL)
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                LOAD_CONST               2 (('retry_on_status',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR                2 (_retry)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_CONST               3 ('ok')
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       351 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(retry_on_status=%(py2)s)\n}._retry\n}(%(py7)s)\n} == %(py12)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py0')
    # |                LOAD_CONST               5 ('backend')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (backend)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('backend')
    # |        L3:     LOAD_CONST               6 ('py2')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('send')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              10 ('send')
    # |        L6:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py12')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_CONST              13 ('assert %(py14)s')
    # |                LOAD_CONST              14 ('py14')
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format15)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
    # |  156           LOAD_DEREF              14 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST              10 (@py_assert0)
    # |                LOAD_SMALL_INT           3
    # |                STORE_FAST_LOAD_FAST    58 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('==',))
    # |                LOAD_FAST_BORROW        11 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 163 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              16 ('py1')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format5)
    # |                LOAD_CONST              17 ('assert %(py6)s')
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_FAST_BORROW        12 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  179 (@py_assert2, @py_assert3)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object send at 0x103bcf0f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 149>:
    # |   --           COPY_FREE_VARS           1
    # |  149           RESUME                   0
    # |  150           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |  151           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           3
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE       12 (to L1)
    # |                NOT_TAKEN
    # |  152           LOAD_GLOBAL              1 (ConnBoom + NULL)
    # |                LOAD_CONST               1 ('Connection error.')
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |  153   L1:     LOAD_CONST               2 ('ok')
    # |                RETURN_VALUE
    # | Disassembly of <code object test_timeout_retried at 0x74af272d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 158>:
    # |   --           MAKE_CELL               10 (ReadTimeout)
    # |                MAKE_CELL               11 (calls)
    # |  158           RESUME                   0
    # |  159           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_CONST               0 (<code object ReadTimeout at 0x103bc31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 159>)
    # |                MAKE_FUNCTION
    # |                LOAD_CONST               1 ('ReadTimeout')
    # |                LOAD_GLOBAL              0 (Exception)
    # |                CALL                     3
    # |                STORE_DEREF             10 (ReadTimeout)
    # |  162           LOAD_CONST               2 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF             11 (calls)
    # |  164           LOAD_FAST_BORROW        10 (ReadTimeout)
    # |                LOAD_FAST_BORROW        11 (calls)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST               3 (<code object send at 0x103c2e630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 164>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |  170           BUILD_LIST               0
    # |                STORE_FAST               2 (@py_assert1)
    # |                LOAD_GLOBAL              3 (backend + NULL)
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                LOAD_CONST               4 (('retry_on_status',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR                4 (_retry)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_CONST               5 ('ok')
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       351 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(retry_on_status=%(py2)s)\n}._retry\n}(%(py7)s)\n} == %(py12)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST               7 ('backend')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (backend)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (backend)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               7 ('backend')
    # |        L3:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py7')
    # |                LOAD_CONST              12 ('send')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              12 ('send')
    # |        L6:     LOAD_CONST              13 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py12')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_CONST              15 ('assert %(py14)s')
    # |                LOAD_CONST              16 ('py14')
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format15)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
    # |                LOAD_CONST              17 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object ReadTimeout at 0x103bc31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 159>:
    # | 159           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestConnectionRetry.test_timeout_retried.<locals>.ReadTimeout')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         159
    # |               STORE_NAME               3 (__firstlineno__)
    # | 160           LOAD_CONST               1 (())
    # |               STORE_NAME               4 (__static_attributes__)
    # |               LOAD_CONST               2 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object send at 0x103c2e630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 164>:
    # |   --           COPY_FREE_VARS           2
    # |  164           RESUME                   0
    # |  165           LOAD_DEREF               1 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |  166           LOAD_DEREF               1 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           2
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE        9 (to L1)
    # |                NOT_TAKEN
    # |  167           LOAD_DEREF               0 (ReadTimeout)
    # |                PUSH_NULL
    # |                LOAD_CONST               1 ('timed out')
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |  168   L1:     LOAD_CONST               2 ('ok')
    # |                RETURN_VALUE
    # | Disassembly of <code object test_can_be_disabled at 0x74af2a4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 172>:
    # |   --           MAKE_CELL                8 (calls)
    # |  172           RESUME                   0
    # |  173           LOAD_CONST               0 ('n')
    # |                LOAD_SMALL_INT           0
    # |                BUILD_MAP                1
    # |                STORE_DEREF              8 (calls)
    # |  175           LOAD_FAST_BORROW         8 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object send at 0x103bc7630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 175>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_FAST               1 (send)
    # |  179           LOAD_GLOBAL              1 (backend + NULL)
    # |                BUILD_LIST               0
    # |                LOAD_CONST               2 (False)
    # |                LOAD_CONST               3 (('retry_on_status', 'retry_on_connection_error'))
    # |                CALL_KW                  2
    # |                STORE_FAST               2 (b)
    # |  180           LOAD_GLOBAL              2 (pytest)
    # |                LOAD_ATTR                4 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (ConnBoom)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  181           LOAD_FAST_BORROW         2 (b)
    # |                LOAD_ATTR                9 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |  180   L2:     LOAD_CONST               4 (None)
    # |                LOAD_CONST               4 (None)
    # |                LOAD_CONST               4 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |  182   L3:     LOAD_DEREF               8 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               3 (@py_assert0)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format5)
    # |                LOAD_CONST               7 ('assert %(py6)s')
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_FAST_BORROW         6 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               4 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               4 (None)
    # |                RETURN_VALUE
    # |  180   L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object send at 0x103bc7630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 175>:
    # |   --           COPY_FREE_VARS           1
    # |  175           RESUME                   0
    # |  176           LOAD_DEREF               0 (calls)
    # |                LOAD_CONST               0 ('n')
    # |                COPY                     2
    # |                COPY                     2
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     3
    # |                SWAP                     2
    # |                STORE_SUBSCR
    # |  177           LOAD_GLOBAL              1 (ConnBoom + NULL)
    # |                LOAD_CONST               1 ('Connection error.')
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # | Disassembly of <code object test_non_connection_error_still_raises at 0x103c492f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 184>:
    # |  184           RESUME                   0
    # |  185           LOAD_CONST               0 (<code object send at 0x103bc33c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 185>)
    # |                MAKE_FUNCTION
    # |                STORE_FAST               1 (send)
    # |  188           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (ValueError)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  189           LOAD_GLOBAL              7 (backend + NULL)
    # |                BUILD_LIST               0
    # |                LOAD_CONST               1 (('retry_on_status',))
    # |                CALL_KW                  1
    # |                LOAD_ATTR                9 (_retry + NULL|self)
    # |                LOAD_FAST_BORROW         1 (send)
    # |                CALL                     1
    # |                POP_TOP
    # |  188   L2:     LOAD_CONST               2 (None)
    # |                LOAD_CONST               2 (None)
    # |                LOAD_CONST               2 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE
    # |        L3:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L4)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L4:     POP_TOP
    # |        L5:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE
    # |   --   L6:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L3 [2] lasti
    # |   L3 to L5 -> L6 [4] lasti
    # | Disassembly of <code object send at 0x103bc33c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 185>:
    # | 185           RESUME                   0
    # | 186           LOAD_GLOBAL              1 (ValueError + NULL)
    # |               LOAD_CONST               0 ('something else')
    # |               CALL                     1
    # |               RAISE_VARARGS            1

    def test_connection_error_retried(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               14 (calls)
        # |  146           RESUME                   0
        # |  147           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF             14 (calls)
        # |  149           LOAD_FAST_BORROW        14 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103bcf0f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 149>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |  155           BUILD_LIST               0
        # |                STORE_FAST               2 (@py_assert1)
        # |                LOAD_GLOBAL              1 (backend + NULL)
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                LOAD_CONST               2 (('retry_on_status',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR                2 (_retry)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_CONST               3 ('ok')
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       351 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(retry_on_status=%(py2)s)\n}._retry\n}(%(py7)s)\n} == %(py12)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py0')
        # |                LOAD_CONST               5 ('backend')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (backend)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('backend')
        # |        L3:     LOAD_CONST               6 ('py2')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('send')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              10 ('send')
        # |        L6:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py12')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_CONST              13 ('assert %(py14)s')
        # |                LOAD_CONST              14 ('py14')
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format15)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
        # |  156           LOAD_DEREF              14 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST              10 (@py_assert0)
        # |                LOAD_SMALL_INT           3
        # |                STORE_FAST_LOAD_FAST    58 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('==',))
        # |                LOAD_FAST_BORROW        11 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 163 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              16 ('py1')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format5)
        # |                LOAD_CONST              17 ('assert %(py6)s')
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_FAST_BORROW        12 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  179 (@py_assert2, @py_assert3)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object send at 0x103bcf0f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 149>:
        # |   --           COPY_FREE_VARS           1
        # |  149           RESUME                   0
        # |  150           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |  151           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           3
        # |                COMPARE_OP              18 (bool(<))
        # |                POP_JUMP_IF_FALSE       12 (to L1)
        # |                NOT_TAKEN
        # |  152           LOAD_GLOBAL              1 (ConnBoom + NULL)
        # |                LOAD_CONST               1 ('Connection error.')
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |  153   L1:     LOAD_CONST               2 ('ok')
        # |                RETURN_VALUE

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |  149           RESUME                   0
            # |  150           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |  151           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           3
            # |                COMPARE_OP              18 (bool(<))
            # |                POP_JUMP_IF_FALSE       12 (to L1)
            # |                NOT_TAKEN
            # |  152           LOAD_GLOBAL              1 (ConnBoom + NULL)
            # |                LOAD_CONST               1 ('Connection error.')
            # |                CALL                     1
            # |                RAISE_VARARGS            1
            # |  153   L1:     LOAD_CONST               2 ('ok')
            # |                RETURN_VALUE


    def test_timeout_retried(self):
        'ReadTimeout'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               10 (ReadTimeout)
        # |                MAKE_CELL               11 (calls)
        # |  158           RESUME                   0
        # |  159           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_CONST               0 (<code object ReadTimeout at 0x103bc31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 159>)
        # |                MAKE_FUNCTION
        # |                LOAD_CONST               1 ('ReadTimeout')
        # |                LOAD_GLOBAL              0 (Exception)
        # |                CALL                     3
        # |                STORE_DEREF             10 (ReadTimeout)
        # |  162           LOAD_CONST               2 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF             11 (calls)
        # |  164           LOAD_FAST_BORROW        10 (ReadTimeout)
        # |                LOAD_FAST_BORROW        11 (calls)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST               3 (<code object send at 0x103c2e630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 164>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |  170           BUILD_LIST               0
        # |                STORE_FAST               2 (@py_assert1)
        # |                LOAD_GLOBAL              3 (backend + NULL)
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                LOAD_CONST               4 (('retry_on_status',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR                4 (_retry)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_CONST               5 ('ok')
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       351 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(retry_on_status=%(py2)s)\n}._retry\n}(%(py7)s)\n} == %(py12)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               6 ('py0')
        # |                LOAD_CONST               7 ('backend')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (backend)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (backend)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               7 ('backend')
        # |        L3:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py7')
        # |                LOAD_CONST              12 ('send')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              12 ('send')
        # |        L6:     LOAD_CONST              13 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py12')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_CONST              15 ('assert %(py14)s')
        # |                LOAD_CONST              16 ('py14')
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format15)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
        # |                LOAD_CONST              17 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object ReadTimeout at 0x103bc31e0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 159>:
        # | 159           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestConnectionRetry.test_timeout_retried.<locals>.ReadTimeout')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         159
        # |               STORE_NAME               3 (__firstlineno__)
        # | 160           LOAD_CONST               1 (())
        # |               STORE_NAME               4 (__static_attributes__)
        # |               LOAD_CONST               2 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object send at 0x103c2e630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 164>:
        # |   --           COPY_FREE_VARS           2
        # |  164           RESUME                   0
        # |  165           LOAD_DEREF               1 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |  166           LOAD_DEREF               1 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           2
        # |                COMPARE_OP              18 (bool(<))
        # |                POP_JUMP_IF_FALSE        9 (to L1)
        # |                NOT_TAKEN
        # |  167           LOAD_DEREF               0 (ReadTimeout)
        # |                PUSH_NULL
        # |                LOAD_CONST               1 ('timed out')
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |  168   L1:     LOAD_CONST               2 ('ok')
        # |                RETURN_VALUE

        class ReadTimeout:
            'TestConnectionRetry.test_timeout_retried.<locals>.ReadTimeout'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 159           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestConnectionRetry.test_timeout_retried.<locals>.ReadTimeout')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         159
            # |               STORE_NAME               3 (__firstlineno__)
            # | 160           LOAD_CONST               1 (())
            # |               STORE_NAME               4 (__static_attributes__)
            # |               LOAD_CONST               2 (None)
            # |               RETURN_VALUE

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           2
            # |  164           RESUME                   0
            # |  165           LOAD_DEREF               1 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |  166           LOAD_DEREF               1 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           2
            # |                COMPARE_OP              18 (bool(<))
            # |                POP_JUMP_IF_FALSE        9 (to L1)
            # |                NOT_TAKEN
            # |  167           LOAD_DEREF               0 (ReadTimeout)
            # |                PUSH_NULL
            # |                LOAD_CONST               1 ('timed out')
            # |                CALL                     1
            # |                RAISE_VARARGS            1
            # |  168   L1:     LOAD_CONST               2 ('ok')
            # |                RETURN_VALUE


    def test_can_be_disabled(self):
        'n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                8 (calls)
        # |  172           RESUME                   0
        # |  173           LOAD_CONST               0 ('n')
        # |                LOAD_SMALL_INT           0
        # |                BUILD_MAP                1
        # |                STORE_DEREF              8 (calls)
        # |  175           LOAD_FAST_BORROW         8 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object send at 0x103bc7630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 175>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_FAST               1 (send)
        # |  179           LOAD_GLOBAL              1 (backend + NULL)
        # |                BUILD_LIST               0
        # |                LOAD_CONST               2 (False)
        # |                LOAD_CONST               3 (('retry_on_status', 'retry_on_connection_error'))
        # |                CALL_KW                  2
        # |                STORE_FAST               2 (b)
        # |  180           LOAD_GLOBAL              2 (pytest)
        # |                LOAD_ATTR                4 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (ConnBoom)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  181           LOAD_FAST_BORROW         2 (b)
        # |                LOAD_ATTR                9 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |  180   L2:     LOAD_CONST               4 (None)
        # |                LOAD_CONST               4 (None)
        # |                LOAD_CONST               4 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |  182   L3:     LOAD_DEREF               8 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               3 (@py_assert0)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 (('==',))
        # |                LOAD_FAST_BORROW         5 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format5)
        # |                LOAD_CONST               7 ('assert %(py6)s')
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_FAST_BORROW         6 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               4 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               4 (None)
        # |                RETURN_VALUE
        # |  180   L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 165 (to L3)
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti
        # | Disassembly of <code object send at 0x103bc7630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 175>:
        # |   --           COPY_FREE_VARS           1
        # |  175           RESUME                   0
        # |  176           LOAD_DEREF               0 (calls)
        # |                LOAD_CONST               0 ('n')
        # |                COPY                     2
        # |                COPY                     2
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     3
        # |                SWAP                     2
        # |                STORE_SUBSCR
        # |  177           LOAD_GLOBAL              1 (ConnBoom + NULL)
        # |                LOAD_CONST               1 ('Connection error.')
        # |                CALL                     1
        # |                RAISE_VARARGS            1

        def send():
            'n'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |  175           RESUME                   0
            # |  176           LOAD_DEREF               0 (calls)
            # |                LOAD_CONST               0 ('n')
            # |                COPY                     2
            # |                COPY                     2
            # |                BINARY_OP               26 ([])
            # |                LOAD_SMALL_INT           1
            # |                BINARY_OP               13 (+=)
            # |                SWAP                     3
            # |                SWAP                     2
            # |                STORE_SUBSCR
            # |  177           LOAD_GLOBAL              1 (ConnBoom + NULL)
            # |                LOAD_CONST               1 ('Connection error.')
            # |                CALL                     1
            # |                RAISE_VARARGS            1


    def test_non_connection_error_still_raises(self):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  184           RESUME                   0
        # |  185           LOAD_CONST               0 (<code object send at 0x103bc33c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 185>)
        # |                MAKE_FUNCTION
        # |                STORE_FAST               1 (send)
        # |  188           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (ValueError)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  189           LOAD_GLOBAL              7 (backend + NULL)
        # |                BUILD_LIST               0
        # |                LOAD_CONST               1 (('retry_on_status',))
        # |                CALL_KW                  1
        # |                LOAD_ATTR                9 (_retry + NULL|self)
        # |                LOAD_FAST_BORROW         1 (send)
        # |                CALL                     1
        # |                POP_TOP
        # |  188   L2:     LOAD_CONST               2 (None)
        # |                LOAD_CONST               2 (None)
        # |                LOAD_CONST               2 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE
        # |        L3:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L4)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L4:     POP_TOP
        # |        L5:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE
        # |   --   L6:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L3 [2] lasti
        # |   L3 to L5 -> L6 [4] lasti
        # | Disassembly of <code object send at 0x103bc33c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 185>:
        # | 185           RESUME                   0
        # | 186           LOAD_GLOBAL              1 (ValueError + NULL)
        # |               LOAD_CONST               0 ('something else')
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def send():
            'something else'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 185           RESUME                   0
            # | 186           LOAD_GLOBAL              1 (ValueError + NULL)
            # |               LOAD_CONST               0 ('something else')
            # |               CALL                     1
            # |               RAISE_VARARGS            1



class TestBackoffWindow:
    'TestBackoffWindow'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 192           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestBackoffWindow')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         192
    # |               STORE_NAME               3 (__firstlineno__)
    # | 193           LOAD_CONST               1 ('号池的坏窗口是分钟级的。退避封顶太小，所有重试会落在同一个窗口里\n一起失败 —— 实测一次卷大纲就是这么挂的。')
    # |               STORE_NAME               4 (__doc__)
    # | 196           LOAD_CONST               2 (<code object test_wait_respects_configured_cap at 0x74af077000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 196>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_wait_respects_configured_cap)
    # | 210           LOAD_CONST               3 (<code object test_default_cap_is_short at 0x74af273200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 210>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_default_cap_is_short)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_wait_respects_configured_cap at 0x74af077000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 196>:
    # |  196            RESUME                   0
    # |  197            BUILD_LIST               0
    # |                 STORE_FAST               2 (waits)
    # |  198            LOAD_FAST_BORROW         1 (monkeypatch)
    # |                 LOAD_ATTR                1 (setattr + NULL|self)
    # |                 LOAD_CONST               0 ('novel_agent.llm.backends.base.time.sleep')
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 LOAD_ATTR                2 (append)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  200            LOAD_CONST               1 (<code object send at 0x103bc34b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 200>)
    # |                 MAKE_FUNCTION
    # |                 STORE_FAST               3 (send)
    # |  204            LOAD_GLOBAL              5 (backend + NULL)
    # |                 LOAD_CONST               2 (403)
    # |                 BUILD_LIST               1
    # |                 LOAD_SMALL_INT           9
    # |                 LOAD_CONST               3 (60.0)
    # |                 LOAD_CONST               4 (('retry_on_status', 'max_retries', 'retry_max_wait'))
    # |                 CALL_KW                  3
    # |                 STORE_FAST               4 (b)
    # |  205            LOAD_GLOBAL              6 (pytest)
    # |                 LOAD_ATTR                8 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             10 (Boom)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |  206            LOAD_FAST_BORROW         4 (b)
    # |                 LOAD_ATTR               13 (_retry + NULL|self)
    # |                 LOAD_FAST_BORROW         3 (send)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  205    L2:     LOAD_CONST               5 (None)
    # |                 LOAD_CONST               5 (None)
    # |                 LOAD_CONST               5 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  207    L3:     LOAD_GLOBAL             15 (max + NULL)
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 LOAD_CONST               6 (8.0)
    # |                 STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         6 (@py_assert5)
    # |                 COMPARE_OP             132 (>)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       312 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              20 (('>',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              21 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} > %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               7 ('py0')
    # |                 LOAD_CONST               8 ('max')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             14 (max)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             14 (max)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               8 ('max')
    # |         L6:     LOAD_CONST               9 ('py1')
    # |                 LOAD_CONST              10 ('waits')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |                 NOT_TAKEN
    # |         L7:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST              10 ('waits')
    # |         L9:     LOAD_CONST              11 ('py3')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py6')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format7)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 ('退避没有超过默认封顶，配置未生效')
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('\n>assert %(py8)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              15 ('py8')
    # |                 LOAD_FAST_BORROW         8 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format9)
    # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST               5 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
    # |  208            LOAD_GLOBAL             35 (sum + NULL)
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 LOAD_SMALL_INT         120
    # |                 STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         6 (@py_assert5)
    # |                 COMPARE_OP             132 (>)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       326 (to L17)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              20 (('>',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              21 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} > %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               7 ('py0')
    # |                 LOAD_CONST              16 ('sum')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             34 (sum)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L12)
    # |                 NOT_TAKEN
    # |        L11:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             34 (sum)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L13)
    # |        L12:     LOAD_CONST              16 ('sum')
    # |        L13:     LOAD_CONST               9 ('py1')
    # |                 LOAD_CONST              10 ('waits')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L14)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L15)
    # |                 NOT_TAKEN
    # |        L14:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L16)
    # |        L15:     LOAD_CONST              10 ('waits')
    # |        L16:     LOAD_CONST              11 ('py3')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py6')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format7)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              17 ('总重试窗口只有 ')
    # |                 LOAD_GLOBAL             35 (sum + NULL)
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 LOAD_CONST              18 ('.0f')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST              19 ('s，跨不过分钟级抖动')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('\n>assert %(py8)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              15 ('py8')
    # |                 LOAD_FAST_BORROW         8 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format9)
    # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L17:     LOAD_CONST               5 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
    # |                 LOAD_CONST               5 (None)
    # |                 RETURN_VALUE
    # |  205   L18:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L19)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L19:     POP_TOP
    # |        L20:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             2
    # |                 JUMP_BACKWARD_NO_INTERRUPT 715 (to L3)
    # |   --   L21:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L18 [2] lasti
    # |   L18 to L20 -> L21 [4] lasti
    # | Disassembly of <code object send at 0x103bc34b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 200>:
    # | 200           RESUME                   0
    # | 201           LOAD_GLOBAL              1 (Boom + NULL)
    # |               LOAD_CONST               0 (403)
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | Disassembly of <code object test_default_cap_is_short at 0x74af273200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 210>:
    # |  210            RESUME                   0
    # |  212            BUILD_LIST               0
    # |                 STORE_FAST               2 (waits)
    # |  213            LOAD_FAST_BORROW         1 (monkeypatch)
    # |                 LOAD_ATTR                1 (setattr + NULL|self)
    # |                 LOAD_CONST               1 ('novel_agent.llm.backends.base.time.sleep')
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 LOAD_ATTR                2 (append)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  215            LOAD_CONST               2 (<code object send at 0x103bc35a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 215>)
    # |                 MAKE_FUNCTION
    # |                 STORE_FAST               3 (send)
    # |  218            LOAD_GLOBAL              4 (pytest)
    # |                 LOAD_ATTR                6 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (Boom)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |  219            LOAD_GLOBAL             11 (backend + NULL)
    # |                 LOAD_CONST               3 (403)
    # |                 BUILD_LIST               1
    # |                 LOAD_SMALL_INT           6
    # |                 LOAD_CONST               4 (('retry_on_status', 'max_retries'))
    # |                 CALL_KW                  2
    # |                 LOAD_ATTR               13 (_retry + NULL|self)
    # |                 LOAD_FAST_BORROW         3 (send)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  218    L2:     LOAD_CONST               5 (None)
    # |                 LOAD_CONST               5 (None)
    # |                 LOAD_CONST               5 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  220    L3:     LOAD_GLOBAL             15 (max + NULL)
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 LOAD_CONST               6 (8.5)
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 COMPARE_OP              42 (<=)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       285 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 (('<=',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              16 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} <= %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               7 ('py0')
    # |                 LOAD_CONST               8 ('max')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             14 (max)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             14 (max)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               8 ('max')
    # |         L6:     LOAD_CONST               9 ('py1')
    # |                 LOAD_CONST              10 ('waits')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |                 NOT_TAKEN
    # |         L7:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (waits)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST              10 ('waits')
    # |         L9:     LOAD_CONST              11 ('py3')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py6')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format7)
    # |                 LOAD_CONST              13 ('assert %(py8)s')
    # |                 LOAD_CONST              14 ('py8')
    # |                 LOAD_FAST_BORROW         7 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format9)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST               5 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
    # |                 LOAD_CONST               5 (None)
    # |                 RETURN_VALUE
    # |  218   L11:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L12)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L12:     POP_TOP
    # |        L13:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD_NO_INTERRUPT 333 (to L3)
    # |   --   L14:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L11 [2] lasti
    # |   L11 to L13 -> L14 [4] lasti
    # | Disassembly of <code object send at 0x103bc35a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 215>:
    # | 215           RESUME                   0
    # | 216           LOAD_GLOBAL              1 (Boom + NULL)
    # |               LOAD_CONST               0 (403)
    # |               CALL                     1
    # |               RAISE_VARARGS            1

    def test_wait_respects_configured_cap(self, monkeypatch):
        'novel_agent.llm.backends.base.time.sleep'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  196            RESUME                   0
        # |  197            BUILD_LIST               0
        # |                 STORE_FAST               2 (waits)
        # |  198            LOAD_FAST_BORROW         1 (monkeypatch)
        # |                 LOAD_ATTR                1 (setattr + NULL|self)
        # |                 LOAD_CONST               0 ('novel_agent.llm.backends.base.time.sleep')
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 LOAD_ATTR                2 (append)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  200            LOAD_CONST               1 (<code object send at 0x103bc34b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 200>)
        # |                 MAKE_FUNCTION
        # |                 STORE_FAST               3 (send)
        # |  204            LOAD_GLOBAL              5 (backend + NULL)
        # |                 LOAD_CONST               2 (403)
        # |                 BUILD_LIST               1
        # |                 LOAD_SMALL_INT           9
        # |                 LOAD_CONST               3 (60.0)
        # |                 LOAD_CONST               4 (('retry_on_status', 'max_retries', 'retry_max_wait'))
        # |                 CALL_KW                  3
        # |                 STORE_FAST               4 (b)
        # |  205            LOAD_GLOBAL              6 (pytest)
        # |                 LOAD_ATTR                8 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             10 (Boom)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |  206            LOAD_FAST_BORROW         4 (b)
        # |                 LOAD_ATTR               13 (_retry + NULL|self)
        # |                 LOAD_FAST_BORROW         3 (send)
        # |                 CALL                     1
        # |                 POP_TOP
        # |  205    L2:     LOAD_CONST               5 (None)
        # |                 LOAD_CONST               5 (None)
        # |                 LOAD_CONST               5 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  207    L3:     LOAD_GLOBAL             15 (max + NULL)
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 LOAD_CONST               6 (8.0)
        # |                 STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         6 (@py_assert5)
        # |                 COMPARE_OP             132 (>)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       312 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              20 (('>',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              21 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} > %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               7 ('py0')
        # |                 LOAD_CONST               8 ('max')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             14 (max)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             14 (max)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               8 ('max')
        # |         L6:     LOAD_CONST               9 ('py1')
        # |                 LOAD_CONST              10 ('waits')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |                 NOT_TAKEN
        # |         L7:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST              10 ('waits')
        # |         L9:     LOAD_CONST              11 ('py3')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py6')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format7)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 ('退避没有超过默认封顶，配置未生效')
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('\n>assert %(py8)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              15 ('py8')
        # |                 LOAD_FAST_BORROW         8 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format9)
        # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST               5 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
        # |  208            LOAD_GLOBAL             35 (sum + NULL)
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 LOAD_SMALL_INT         120
        # |                 STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         6 (@py_assert5)
        # |                 COMPARE_OP             132 (>)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       326 (to L17)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              20 (('>',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              21 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} > %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               7 ('py0')
        # |                 LOAD_CONST              16 ('sum')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             34 (sum)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L12)
        # |                 NOT_TAKEN
        # |        L11:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             34 (sum)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L13)
        # |        L12:     LOAD_CONST              16 ('sum')
        # |        L13:     LOAD_CONST               9 ('py1')
        # |                 LOAD_CONST              10 ('waits')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L14)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L15)
        # |                 NOT_TAKEN
        # |        L14:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L16)
        # |        L15:     LOAD_CONST              10 ('waits')
        # |        L16:     LOAD_CONST              11 ('py3')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py6')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format7)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              17 ('总重试窗口只有 ')
        # |                 LOAD_GLOBAL             35 (sum + NULL)
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 LOAD_CONST              18 ('.0f')
        # |                 FORMAT_WITH_SPEC
        # |                 LOAD_CONST              19 ('s，跨不过分钟级抖动')
        # |                 BUILD_STRING             3
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('\n>assert %(py8)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              15 ('py8')
        # |                 LOAD_FAST_BORROW         8 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format9)
        # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L17:     LOAD_CONST               5 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
        # |                 LOAD_CONST               5 (None)
        # |                 RETURN_VALUE
        # |  205   L18:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L19)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L19:     POP_TOP
        # |        L20:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             2
        # |                 JUMP_BACKWARD_NO_INTERRUPT 715 (to L3)
        # |   --   L21:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L18 [2] lasti
        # |   L18 to L20 -> L21 [4] lasti
        # | Disassembly of <code object send at 0x103bc34b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 200>:
        # | 200           RESUME                   0
        # | 201           LOAD_GLOBAL              1 (Boom + NULL)
        # |               LOAD_CONST               0 (403)
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def send():
            pass  # 无 docstring
            # ── 函数体（字节码重建见 BODY 段）──
            # | 200           RESUME                   0
            # | 201           LOAD_GLOBAL              1 (Boom + NULL)
            # |               LOAD_CONST               0 (403)
            # |               CALL                     1
            # |               RAISE_VARARGS            1


    def test_default_cap_is_short(self, monkeypatch):
        '默认值保持小 —— 只有已知不稳的渠道才该配长窗口。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  210            RESUME                   0
        # |  212            BUILD_LIST               0
        # |                 STORE_FAST               2 (waits)
        # |  213            LOAD_FAST_BORROW         1 (monkeypatch)
        # |                 LOAD_ATTR                1 (setattr + NULL|self)
        # |                 LOAD_CONST               1 ('novel_agent.llm.backends.base.time.sleep')
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 LOAD_ATTR                2 (append)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  215            LOAD_CONST               2 (<code object send at 0x103bc35a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 215>)
        # |                 MAKE_FUNCTION
        # |                 STORE_FAST               3 (send)
        # |  218            LOAD_GLOBAL              4 (pytest)
        # |                 LOAD_ATTR                6 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (Boom)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |  219            LOAD_GLOBAL             11 (backend + NULL)
        # |                 LOAD_CONST               3 (403)
        # |                 BUILD_LIST               1
        # |                 LOAD_SMALL_INT           6
        # |                 LOAD_CONST               4 (('retry_on_status', 'max_retries'))
        # |                 CALL_KW                  2
        # |                 LOAD_ATTR               13 (_retry + NULL|self)
        # |                 LOAD_FAST_BORROW         3 (send)
        # |                 CALL                     1
        # |                 POP_TOP
        # |  218    L2:     LOAD_CONST               5 (None)
        # |                 LOAD_CONST               5 (None)
        # |                 LOAD_CONST               5 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  220    L3:     LOAD_GLOBAL             15 (max + NULL)
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 LOAD_CONST               6 (8.5)
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 COMPARE_OP              42 (<=)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       285 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 (('<=',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              16 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} <= %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               7 ('py0')
        # |                 LOAD_CONST               8 ('max')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             14 (max)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             14 (max)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               8 ('max')
        # |         L6:     LOAD_CONST               9 ('py1')
        # |                 LOAD_CONST              10 ('waits')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |                 NOT_TAKEN
        # |         L7:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (waits)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST              10 ('waits')
        # |         L9:     LOAD_CONST              11 ('py3')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py6')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format7)
        # |                 LOAD_CONST              13 ('assert %(py8)s')
        # |                 LOAD_CONST              14 ('py8')
        # |                 LOAD_FAST_BORROW         7 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format9)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST               5 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
        # |                 LOAD_CONST               5 (None)
        # |                 RETURN_VALUE
        # |  218   L11:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L12)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L12:     POP_TOP
        # |        L13:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD_NO_INTERRUPT 333 (to L3)
        # |   --   L14:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L11 [2] lasti
        # |   L11 to L13 -> L14 [4] lasti
        # | Disassembly of <code object send at 0x103bc35a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_retry.py", line 215>:
        # | 215           RESUME                   0
        # | 216           LOAD_GLOBAL              1 (Boom + NULL)
        # |               LOAD_CONST               0 (403)
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def send():
            pass  # 无 docstring
            # ── 函数体（字节码重建见 BODY 段）──
            # | 215           RESUME                   0
            # | 216           LOAD_GLOBAL              1 (Boom + NULL)
            # |               LOAD_CONST               0 (403)
            # |               CALL                     1
            # |               RAISE_VARARGS            1


