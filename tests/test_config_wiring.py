# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py
# 来源   : test_config_wiring.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '当前的供应商接线是否符合意图。\n\n这些断言把"哪个角色用哪家"钉死。改动路由是有代价的决定（文风一致性、\n成本、缓存），不应该被顺手改掉而没人注意。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '当前的供应商接线是否符合意图。\n\n这些断言把"哪个角色用哪家"钉死。改动路由是有代价的决定（文风一致性、\n成本、缓存），不应该被顺手改掉而没人注意。\n',
    7: 'config',
    8: 'models.yaml',
    12: 'TestRoleSplit',
    14: 'TestPackyapiWiring',
    16: 'TestAuthStyle',
    18: 'TestNoSecretsInRepo',
    20: 'TestFailoverChain',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'Router',
    ('TestRoleSplit', 0): 'TestRoleSplit',
    ('TestRoleSplit', 2): 'role',
    ('test_stitcher_matches_writer', 0): 'stitcher 是最后一道经手正文的工序。与 writer 不同源会让文风打架。',
    ('test_stitcher_matches_writer', 1): 'stitcher',
    ('test_stitcher_matches_writer', 2): 'writer',
    ('test_stitcher_matches_writer', 3): 'py0',
    ('test_stitcher_matches_writer', 4): 'router',
    ('test_stitcher_matches_writer', 5): 'py2',
    ('test_stitcher_matches_writer', 6): 'py4',
    ('test_stitcher_matches_writer', 7): 'py6',
    ('test_stitcher_matches_writer', 8): 'py8',
    ('test_stitcher_matches_writer', 9): 'py10',
    ('test_stitcher_matches_writer', 10): 'py12',
    ('test_stitcher_matches_writer', 11): 'py14',
    ('test_stitcher_matches_writer', 12): 'py16',
    ('test_stitcher_matches_writer', 13): 'py18',
    ('test_stitcher_matches_writer', 14): 'assert %(py20)s',
    ('test_stitcher_matches_writer', 15): 'py20',
    ('test_structured_roles_use_cheap_provider', 0): 'deepseek',
    ('test_structured_roles_use_cheap_provider', 1): 'py0',
    ('test_structured_roles_use_cheap_provider', 2): 'router',
    ('test_structured_roles_use_cheap_provider', 3): 'py2',
    ('test_structured_roles_use_cheap_provider', 4): 'py3',
    ('test_structured_roles_use_cheap_provider', 5): 'role',
    ('test_structured_roles_use_cheap_provider', 6): 'py5',
    ('test_structured_roles_use_cheap_provider', 7): 'py7',
    ('test_structured_roles_use_cheap_provider', 8): 'py10',
    ('test_structured_roles_use_cheap_provider', 9): 'assert %(py12)s',
    ('test_structured_roles_use_cheap_provider', 10): 'py12',
    ('TestPackyapiWiring', 0): 'TestPackyapiWiring',
    ('test_uses_bearer_not_x_api_key', 0): '中转站要 Authorization: Bearer，官方才是 x-api-key。搞错必然 401。',
    ('test_uses_bearer_not_x_api_key', 1): 'packyapi',
    ('test_uses_bearer_not_x_api_key', 2): 'bearer',
    ('test_uses_bearer_not_x_api_key', 3): 'py0',
    ('test_uses_bearer_not_x_api_key', 4): 'router',
    ('test_uses_bearer_not_x_api_key', 5): 'py2',
    ('test_uses_bearer_not_x_api_key', 6): 'py4',
    ('test_uses_bearer_not_x_api_key', 7): 'py6',
    ('test_uses_bearer_not_x_api_key', 8): 'py8',
    ('test_uses_bearer_not_x_api_key', 9): 'py11',
    ('test_uses_bearer_not_x_api_key', 10): 'assert %(py13)s',
    ('test_uses_bearer_not_x_api_key', 11): 'py13',
    ('test_native_anthropic_endpoint', 0): '必须走 anthropic 原生协议 —— cache_control 只在这条路上有效。',
    ('test_native_anthropic_endpoint', 1): 'packyapi',
    ('test_native_anthropic_endpoint', 2): 'anthropic',
    ('test_native_anthropic_endpoint', 3): 'py0',
    ('test_native_anthropic_endpoint', 4): 'cfg',
    ('test_native_anthropic_endpoint', 5): 'py2',
    ('test_native_anthropic_endpoint', 6): 'py5',
    ('test_native_anthropic_endpoint', 7): 'assert %(py7)s',
    ('test_native_anthropic_endpoint', 8): 'py7',
    ('test_native_anthropic_endpoint', 10): 'https://cf.api.fan',
    ('test_secret_read_from_env_not_hardcoded', 0): 'packyapi',
    ('test_secret_read_from_env_not_hardcoded', 1): 'PACKYAPI_AUTH_TOKEN',
    ('test_secret_read_from_env_not_hardcoded', 2): 'py0',
    ('test_secret_read_from_env_not_hardcoded', 3): 'cfg',
    ('test_secret_read_from_env_not_hardcoded', 4): 'py2',
    ('test_secret_read_from_env_not_hardcoded', 5): 'py5',
    ('test_secret_read_from_env_not_hardcoded', 6): 'assert %(py7)s',
    ('test_secret_read_from_env_not_hardcoded', 7): 'py7',
    ('test_secret_read_from_env_not_hardcoded', 9): 'utf-8',
    ('test_secret_read_from_env_not_hardcoded', 10): 'sk-',
    ('test_secret_read_from_env_not_hardcoded', 11): 'py1',
    ('test_secret_read_from_env_not_hardcoded', 12): 'py3',
    ('test_secret_read_from_env_not_hardcoded', 13): 'raw',
    ('test_secret_read_from_env_not_hardcoded', 14): '配置文件里出现了疑似密钥，密钥只能放 .env',
    ('test_secret_read_from_env_not_hardcoded', 15): '\n>assert %(py5)s',
    ('test_fallback_group_defined', 0): 'cc-sale 缓存异常时的退路必须配好，不用临时现查。',
    ('test_fallback_group_defined', 1): 'packyapi_awsq',
    ('test_fallback_group_defined', 2): 'https://cf.api.fan',
    ('test_fallback_group_defined', 3): 'py0',
    ('test_fallback_group_defined', 4): 'awsq',
    ('test_fallback_group_defined', 5): 'py2',
    ('test_fallback_group_defined', 6): 'py5',
    ('test_fallback_group_defined', 7): 'assert %(py7)s',
    ('test_fallback_group_defined', 8): 'py7',
    ('test_fallback_group_defined', 10): 'bearer',
    ('test_awsq_retries_422', 0): 'aws-q 官方警告"容易出现 422"，而 SDK 默认不重试 422。',
    ('test_awsq_retries_422', 2): 'packyapi_awsq',
    ('test_awsq_retries_422', 3): 'py1',
    ('test_awsq_retries_422', 4): 'py3',
    ('test_awsq_retries_422', 5): 'router',
    ('test_awsq_retries_422', 6): 'py5',
    ('test_awsq_retries_422', 7): 'py7',
    ('test_awsq_retries_422', 8): 'py9',
    ('test_awsq_retries_422', 9): 'py11',
    ('test_awsq_retries_422', 10): 'assert %(py13)s',
    ('test_awsq_retries_422', 11): 'py13',
    ('test_retry_list_excludes_sdk_handled_codes', 0): 'SDK 已重试 408/409/429 与全部 5xx，重复列会导致乘法重试。',
    ('test_retry_list_excludes_sdk_handled_codes', 1): 'packyapi_awsq',
    ('test_retry_list_excludes_sdk_handled_codes', 2): '这些码 SDK 已处理，不该再列：',
    ('test_retry_list_excludes_sdk_handled_codes', 3): '\n>assert not %(py0)s',
    ('test_retry_list_excludes_sdk_handled_codes', 4): 'py0',
    ('test_retry_list_excludes_sdk_handled_codes', 5): 'overlap',
    ('test_primary_group_retries_transient_403', 0): '实测 cc-sale 号池会间歇性返回 403（上游账号失效的转述）。\n\nSDK 按语义把 403 当永久拒绝、不重试，所以必须显式加。\n',
    ('test_primary_group_retries_transient_403', 1): 'packyapi',
    ('test_primary_group_retries_transient_403', 3): 'py1',
    ('test_primary_group_retries_transient_403', 4): 'py3',
    ('test_primary_group_retries_transient_403', 5): 'cfg',
    ('test_primary_group_retries_transient_403', 6): 'py5',
    ('test_primary_group_retries_transient_403', 7): 'assert %(py7)s',
    ('test_primary_group_retries_transient_403', 8): 'py7',
    ('test_primary_group_retries_transient_403', 10): 'py0',
    ('test_primary_group_retries_transient_403', 11): 'py2',
    ('test_primary_group_retries_transient_403', 12): '成功率低时重试次数太少等于没加',
    ('test_primary_group_retries_transient_403', 13): '\n>assert %(py7)s',
    ('TestAuthStyle', 0): 'TestAuthStyle',
    ('__annotate__', 1): 'style',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('_client_kwargs', 1): 'FakeAnthropic',
    ('_client_kwargs', 3): 'Anthropic',
    ('_client_kwargs', 4): 'TEST_SECRET',
    ('_client_kwargs', 5): 'sk-test-secret-value',
    ('_client_kwargs', 6): 't',
    ('_client_kwargs', 7): 'anthropic',
    ('_client_kwargs', 8): 'https://cf.api.fan',
    ('FakeAnthropic', 0): 'TestAuthStyle._client_kwargs.<locals>.FakeAnthropic',
    ('test_bearer_uses_auth_token', 0): 'bearer',
    ('test_bearer_uses_auth_token', 1): 'auth_token',
    ('test_bearer_uses_auth_token', 2): 'sk-test-secret-value',
    ('test_bearer_uses_auth_token', 3): 'py0',
    ('test_bearer_uses_auth_token', 4): 'kw',
    ('test_bearer_uses_auth_token', 5): 'py2',
    ('test_bearer_uses_auth_token', 6): 'py4',
    ('test_bearer_uses_auth_token', 7): 'py6',
    ('test_bearer_uses_auth_token', 8): 'py9',
    ('test_bearer_uses_auth_token', 9): 'assert %(py11)s',
    ('test_bearer_uses_auth_token', 10): 'py11',
    ('test_bearer_uses_auth_token', 12): 'api_key',
    ('test_bearer_uses_auth_token', 13): 'py1',
    ('test_bearer_uses_auth_token', 14): 'py3',
    ('test_bearer_uses_auth_token', 15): 'assert %(py5)s',
    ('test_bearer_uses_auth_token', 16): 'py5',
    ('test_api_key_style_uses_api_key', 0): 'api_key',
    ('test_api_key_style_uses_api_key', 1): 'sk-test-secret-value',
    ('test_api_key_style_uses_api_key', 2): 'py0',
    ('test_api_key_style_uses_api_key', 3): 'kw',
    ('test_api_key_style_uses_api_key', 4): 'py2',
    ('test_api_key_style_uses_api_key', 5): 'py4',
    ('test_api_key_style_uses_api_key', 6): 'py6',
    ('test_api_key_style_uses_api_key', 7): 'py9',
    ('test_api_key_style_uses_api_key', 8): 'assert %(py11)s',
    ('test_api_key_style_uses_api_key', 9): 'py11',
    ('test_api_key_style_uses_api_key', 11): 'auth_token',
    ('test_api_key_style_uses_api_key', 12): 'py1',
    ('test_api_key_style_uses_api_key', 13): 'py3',
    ('test_api_key_style_uses_api_key', 14): 'assert %(py5)s',
    ('test_api_key_style_uses_api_key', 15): 'py5',
    ('test_base_url_forwarded', 0): 'bearer',
    ('test_base_url_forwarded', 1): 'base_url',
    ('test_base_url_forwarded', 2): 'https://cf.api.fan',
    ('test_base_url_forwarded', 3): 'py1',
    ('test_base_url_forwarded', 4): 'py4',
    ('test_base_url_forwarded', 5): 'assert %(py6)s',
    ('test_base_url_forwarded', 6): 'py6',
    ('TestNoSecretsInRepo', 0): 'TestNoSecretsInRepo',
    ('test_no_keys_committed', 0): '密钥只能存在于 .env（已 gitignore）。',
    ('test_no_keys_committed', 1): 'config/*.yaml',
    ('test_no_keys_committed', 2): '.env.example',
    ('test_no_keys_committed', 3): 'README.md',
    ('test_no_keys_committed', 4): 'utf-8',
    ('test_no_keys_committed', 5): 'sk-',
    ('test_no_keys_committed', 9): '=',
    ('test_no_keys_committed', 10): '#',
    ('test_no_keys_committed', 11): ':',
    ('test_no_keys_committed', 12): ' 变量 ',
    ('test_no_keys_committed', 13): ' 疑似含真实密钥。真实密钥只能放 .env（已 gitignore），本文件只放占位符。',
    ('test_no_keys_committed', 14): '\n>assert %(py0)s',
    ('test_no_keys_committed', 15): 'py0',
    ('test_no_keys_committed', 16): 'placeholder',
    ('TestFailoverChain', 0): 'TestFailoverChain',
    ('TestFailoverChain', 1): '号池型渠道会整段时间不可用，重试再多也落在同一个坏窗口里。\n实测一次卷大纲把 9 次重试全用完仍然失败 —— 必须能换链路。',
    ('test_creative_roles_have_fallbacks', 0): ' 没有降级链，主渠道挂了就整轮死',
    ('test_creative_roles_have_fallbacks', 1): '\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}',
    ('test_creative_roles_have_fallbacks', 2): 'py0',
    ('test_creative_roles_have_fallbacks', 3): 'router',
    ('test_creative_roles_have_fallbacks', 4): 'py2',
    ('test_creative_roles_have_fallbacks', 5): 'py3',
    ('test_creative_roles_have_fallbacks', 6): 'role',
    ('test_creative_roles_have_fallbacks', 7): 'py5',
    ('test_creative_roles_have_fallbacks', 8): 'py7',
    ('test_prose_roles_use_one_model', 1): 'py0',
    ('test_prose_roles_use_one_model', 2): 'len',
    ('test_prose_roles_use_one_model', 3): 'py1',
    ('test_prose_roles_use_one_model', 4): 'models',
    ('test_prose_roles_use_one_model', 5): 'py3',
    ('test_prose_roles_use_one_model', 6): 'py6',
    ('test_prose_roles_use_one_model', 7): '创作链路用了多个模型：',
    ('test_prose_roles_use_one_model', 8): '\n>assert %(py8)s',
    ('test_prose_roles_use_one_model', 9): 'py8',
    ('test_writer_and_stitcher_share_the_fallback_chain', 0): '缝合与写作必须同进同退。若 writer 降级了而 stitcher 没有，\n同一章的正文和接缝就出自两支笔。',
    ('test_writer_and_stitcher_share_the_fallback_chain', 1): 'writer',
    ('test_writer_and_stitcher_share_the_fallback_chain', 2): 'stitcher',
    ('test_writer_and_stitcher_share_the_fallback_chain', 3): 'py0',
    ('test_writer_and_stitcher_share_the_fallback_chain', 4): 'router',
    ('test_writer_and_stitcher_share_the_fallback_chain', 5): 'py2',
    ('test_writer_and_stitcher_share_the_fallback_chain', 6): 'py4',
    ('test_writer_and_stitcher_share_the_fallback_chain', 7): 'py6',
    ('test_writer_and_stitcher_share_the_fallback_chain', 8): 'py8',
    ('test_writer_and_stitcher_share_the_fallback_chain', 9): 'py10',
    ('test_writer_and_stitcher_share_the_fallback_chain', 10): 'py12',
    ('test_writer_and_stitcher_share_the_fallback_chain', 11): 'py14',
    ('test_writer_and_stitcher_share_the_fallback_chain', 12): 'py16',
    ('test_writer_and_stitcher_share_the_fallback_chain', 13): 'py18',
    ('test_writer_and_stitcher_share_the_fallback_chain', 14): 'assert %(py20)s',
    ('test_writer_and_stitcher_share_the_fallback_chain', 15): 'py20',
    ('test_codex_group_is_not_wired_to_any_role', 0): 'codex 分组明文禁止第三方接入并主动封锁非 Codex 客户端。\n实测 8 种协议/模型组合全被拒。配置保留只为记录，不能指过来。',
    ('test_codex_group_is_not_wired_to_any_role', 1): 'packyapi_codex',
    ('test_codex_group_is_not_wired_to_any_role', 2): 'py1',
    ('test_codex_group_is_not_wired_to_any_role', 3): 'py3',
    ('test_codex_group_is_not_wired_to_any_role', 4): 'chain',
    ('test_codex_group_is_not_wired_to_any_role', 5): ' 指向了被禁止的 codex 分组',
    ('test_codex_group_is_not_wired_to_any_role', 6): '\n>assert %(py5)s',
    ('test_codex_group_is_not_wired_to_any_role', 7): 'py5',
    ('test_fallbacks_avoid_the_primary_pool', 0): '降级目标不能和主渠道是同一个池子 —— 那等于没降级。',
    ('test_fallbacks_avoid_the_primary_pool', 2): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_fallbacks_avoid_the_primary_pool', 3): 'py0',
    ('test_fallbacks_avoid_the_primary_pool', 4): 'all',
    ('test_fallbacks_avoid_the_primary_pool', 5): 'py2',
    ('test_fallbacks_avoid_the_primary_pool', 6): 'py4',
    ('test_every_creative_role_has_a_fallback', 0): ' 没有降级链',
    ('test_every_creative_role_has_a_fallback', 1): '\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}',
    ('test_every_creative_role_has_a_fallback', 2): 'py0',
    ('test_every_creative_role_has_a_fallback', 3): 'router',
    ('test_every_creative_role_has_a_fallback', 4): 'py2',
    ('test_every_creative_role_has_a_fallback', 5): 'py3',
    ('test_every_creative_role_has_a_fallback', 6): 'role',
    ('test_every_creative_role_has_a_fallback', 7): 'py5',
    ('test_every_creative_role_has_a_fallback', 8): 'py7',
    ('test_fallback_providers_are_defined', 1): 'py0',
    ('test_fallback_providers_are_defined', 2): 'router',
    ('test_fallback_providers_are_defined', 3): 'py2',
    ('test_fallback_providers_are_defined', 4): 'py3',
    ('test_fallback_providers_are_defined', 5): 'provider',
    ('test_fallback_providers_are_defined', 6): 'py5',
    ('test_fallback_providers_are_defined', 7): 'py8',
    ('test_fallback_providers_are_defined', 8): 'assert %(py10)s',
    ('test_fallback_providers_are_defined', 9): 'py10',
    ('test_unknown_fallback_provider_fails_loudly', 3): 'm.yaml',
    ('test_unknown_fallback_provider_fails_loudly', 4): 'default_provider',
    ('test_unknown_fallback_provider_fails_loudly', 5): 'a',
    ('test_unknown_fallback_provider_fails_loudly', 6): 'providers',
    ('test_unknown_fallback_provider_fails_loudly', 7): 'kind',
    ('test_unknown_fallback_provider_fails_loudly', 8): 'anthropic',
    ('test_unknown_fallback_provider_fails_loudly', 9): 'api_key_env',
    ('test_unknown_fallback_provider_fails_loudly', 10): 'K',
    ('test_unknown_fallback_provider_fails_loudly', 11): 'roles',
    ('test_unknown_fallback_provider_fails_loudly', 12): 'writer',
    ('test_unknown_fallback_provider_fails_loudly', 13): 'model',
    ('test_unknown_fallback_provider_fails_loudly', 14): 'm',
    ('test_unknown_fallback_provider_fails_loudly', 15): 'max_tokens',
    ('test_unknown_fallback_provider_fails_loudly', 16): 'fallbacks',
    ('test_unknown_fallback_provider_fails_loudly', 17): 'provider',
    ('test_unknown_fallback_provider_fails_loudly', 18): 'typo',
    ('test_unknown_fallback_provider_fails_loudly', 19): 'cache_multipliers',
    ('test_unknown_fallback_provider_fails_loudly', 20): 'read',
    ('test_unknown_fallback_provider_fails_loudly', 22): 'write_5m',
    ('test_unknown_fallback_provider_fails_loudly', 24): 'write_1h',
    ('test_unknown_fallback_provider_fails_loudly', 26): 'utf-8',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def router():
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  25           RESUME                   0
    # |  27           LOAD_GLOBAL              1 (Router + NULL)
    # |               LOAD_GLOBAL              2 (CONFIG)
    # |               CALL                     1
    # |               RETURN_VALUE

class TestRoleSplit:
    'TestRoleSplit'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  30           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRoleSplit')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          30
    # |               STORE_NAME               3 (__firstlineno__)
    # |  33           LOAD_CONST               1 (<code object test_stitcher_matches_writer at 0x78a91e4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 33>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_stitcher_matches_writer)
    # |  38           LOAD_NAME                5 (pytest)
    # |               LOAD_ATTR               12 (mark)
    # |               LOAD_ATTR               15 (parametrize + NULL|self)
    # |               LOAD_CONST               2 ('role')
    # |               LOAD_NAME                8 (STRUCTURED_ROLES)
    # |               CALL                     2
    # |  39           LOAD_CONST               3 (<code object test_structured_roles_use_cheap_provider at 0x78a9215c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 38>)
    # |               MAKE_FUNCTION
    # |  38           CALL                     0
    # |  39           STORE_NAME               9 (test_structured_roles_use_cheap_provider)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_stitcher_matches_writer at 0x78a91e4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 33>:
    # |  33            RESUME                   0
    # |  35            LOAD_FAST_BORROW         1 (router)
    # |                LOAD_ATTR                0 (for_role)
    # |                STORE_FAST               2 (@py_assert1)
    # |                LOAD_CONST               1 ('stitcher')
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                LOAD_ATTR                2 (model)
    # |                STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
    # |                LOAD_ATTR                0 (for_role)
    # |                STORE_FAST               6 (@py_assert11)
    # |                LOAD_CONST               2 ('writer')
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
    # |                LOAD_ATTR                2 (model)
    # |                STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
    # |                LOAD_FAST_BORROW         9 (@py_assert17)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       409 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert9)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.model\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.model\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('router')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('router')
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
    # |                LOAD_CONST               7 ('py6')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py8')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py10')
    # |                LOAD_CONST               4 ('router')
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
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('router')
    # |        L6:     LOAD_CONST              10 ('py12')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py14')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py16')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert15)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py18')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert17)
    # |                CALL                     1
    # |                BUILD_MAP               10
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format19)
    # |                LOAD_CONST              14 ('assert %(py20)s')
    # |                LOAD_CONST              15 ('py20')
    # |                LOAD_FAST_BORROW        11 (@py_format19)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format21)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format21)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              16 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert13)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
    # |  36            LOAD_FAST_BORROW         1 (router)
    # |                LOAD_ATTR                0 (for_role)
    # |                STORE_FAST               2 (@py_assert1)
    # |                LOAD_CONST               1 ('stitcher')
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                LOAD_ATTR               20 (provider)
    # |                STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
    # |                LOAD_ATTR                0 (for_role)
    # |                STORE_FAST               6 (@py_assert11)
    # |                LOAD_CONST               2 ('writer')
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
    # |                LOAD_ATTR               20 (provider)
    # |                STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
    # |                LOAD_FAST_BORROW         9 (@py_assert17)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       409 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert9)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.provider\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.provider\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('router')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               4 ('router')
    # |       L10:     LOAD_CONST               5 ('py2')
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
    # |                LOAD_CONST               7 ('py6')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py8')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py10')
    # |                LOAD_CONST               4 ('router')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST               4 ('router')
    # |       L13:     LOAD_CONST              10 ('py12')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py14')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py16')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert15)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py18')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert17)
    # |                CALL                     1
    # |                BUILD_MAP               10
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format19)
    # |                LOAD_CONST              14 ('assert %(py20)s')
    # |                LOAD_CONST              15 ('py20')
    # |                LOAD_FAST_BORROW        11 (@py_format19)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format21)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format21)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST              16 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert13)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
    # |                LOAD_CONST              16 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_structured_roles_use_cheap_provider at 0x78a9215c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 38>:
    # |  38           RESUME                   0
    # |  40           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                0 (for_role)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |               LOAD_ATTR                2 (provider)
    # |               STORE_FAST               5 (@py_assert6)
    # |               LOAD_CONST               0 ('deepseek')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert9, @py_assert6)
    # |               LOAD_FAST_BORROW         6 (@py_assert9)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert8, @py_assert8)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       321 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.provider\n} == %(py10)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert6, @py_assert9)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('router')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('router')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('role')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               5 ('role')
    # |       L6:     LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py10')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert9)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format11)
    # |               LOAD_CONST               9 ('assert %(py12)s')
    # |               LOAD_CONST              10 ('py12')
    # |               LOAD_FAST_BORROW         8 (@py_format11)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format13)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format13)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  118 (@py_assert8, @py_assert9)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE

    def test_stitcher_matches_writer(self, router):
        'stitcher 是最后一道经手正文的工序。与 writer 不同源会让文风打架。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  33            RESUME                   0
        # |  35            LOAD_FAST_BORROW         1 (router)
        # |                LOAD_ATTR                0 (for_role)
        # |                STORE_FAST               2 (@py_assert1)
        # |                LOAD_CONST               1 ('stitcher')
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                LOAD_ATTR                2 (model)
        # |                STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
        # |                LOAD_ATTR                0 (for_role)
        # |                STORE_FAST               6 (@py_assert11)
        # |                LOAD_CONST               2 ('writer')
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
        # |                LOAD_ATTR                2 (model)
        # |                STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
        # |                LOAD_FAST_BORROW         9 (@py_assert17)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       409 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert9)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.model\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.model\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('router')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('router')
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
        # |                LOAD_CONST               7 ('py6')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py8')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py10')
        # |                LOAD_CONST               4 ('router')
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
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('router')
        # |        L6:     LOAD_CONST              10 ('py12')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py14')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py16')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert15)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py18')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert17)
        # |                CALL                     1
        # |                BUILD_MAP               10
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format19)
        # |                LOAD_CONST              14 ('assert %(py20)s')
        # |                LOAD_CONST              15 ('py20')
        # |                LOAD_FAST_BORROW        11 (@py_format19)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format21)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format21)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              16 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert13)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
        # |  36            LOAD_FAST_BORROW         1 (router)
        # |                LOAD_ATTR                0 (for_role)
        # |                STORE_FAST               2 (@py_assert1)
        # |                LOAD_CONST               1 ('stitcher')
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                LOAD_ATTR               20 (provider)
        # |                STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
        # |                LOAD_ATTR                0 (for_role)
        # |                STORE_FAST               6 (@py_assert11)
        # |                LOAD_CONST               2 ('writer')
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
        # |                LOAD_ATTR               20 (provider)
        # |                STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
        # |                LOAD_FAST_BORROW         9 (@py_assert17)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       409 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert9)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.provider\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.provider\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('router')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               4 ('router')
        # |       L10:     LOAD_CONST               5 ('py2')
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
        # |                LOAD_CONST               7 ('py6')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py8')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py10')
        # |                LOAD_CONST               4 ('router')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST               4 ('router')
        # |       L13:     LOAD_CONST              10 ('py12')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py14')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py16')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert15)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py18')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert17)
        # |                CALL                     1
        # |                BUILD_MAP               10
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format19)
        # |                LOAD_CONST              14 ('assert %(py20)s')
        # |                LOAD_CONST              15 ('py20')
        # |                LOAD_FAST_BORROW        11 (@py_format19)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format21)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format21)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST              16 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert13)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
        # |                LOAD_CONST              16 (None)
        # |                RETURN_VALUE

    def test_structured_roles_use_cheap_provider(self, router, role):
        'deepseek'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  38           RESUME                   0
        # |  40           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                0 (for_role)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |               LOAD_ATTR                2 (provider)
        # |               STORE_FAST               5 (@py_assert6)
        # |               LOAD_CONST               0 ('deepseek')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert9, @py_assert6)
        # |               LOAD_FAST_BORROW         6 (@py_assert9)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert8, @py_assert8)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       321 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.provider\n} == %(py10)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert6, @py_assert9)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('router')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('router')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('role')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               5 ('role')
        # |       L6:     LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py10')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert9)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format11)
        # |               LOAD_CONST               9 ('assert %(py12)s')
        # |               LOAD_CONST              10 ('py12')
        # |               LOAD_FAST_BORROW         8 (@py_format11)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format13)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format13)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  118 (@py_assert8, @py_assert9)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE


class TestPackyapiWiring:
    'TestPackyapiWiring'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  43           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPackyapiWiring')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          43
    # |               STORE_NAME               3 (__firstlineno__)
    # |  44           LOAD_CONST               1 (<code object test_uses_bearer_not_x_api_key at 0x78a8e68700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 44>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_uses_bearer_not_x_api_key)
    # |  48           LOAD_CONST               2 (<code object test_native_anthropic_endpoint at 0x78a91fd400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 48>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_native_anthropic_endpoint)
    # |  54           LOAD_CONST               3 (<code object test_secret_read_from_env_not_hardcoded at 0x78a91fed00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 54>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_secret_read_from_env_not_hardcoded)
    # |  60           LOAD_CONST               4 (<code object test_fallback_group_defined at 0x78a91ff200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 60>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_fallback_group_defined)
    # |  66           LOAD_CONST               5 (<code object test_awsq_retries_422 at 0x78a8e68a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 66>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_awsq_retries_422)
    # |  70           LOAD_CONST               6 (<code object test_retry_list_excludes_sdk_handled_codes at 0x78a9213900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 70>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_retry_list_excludes_sdk_handled_codes)
    # |  76           LOAD_CONST               7 (<code object test_primary_group_retries_transient_403 at 0x78a90c3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 76>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_primary_group_retries_transient_403)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_uses_bearer_not_x_api_key at 0x78a8e68700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 44>:
    # |  44           RESUME                   0
    # |  46           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                0 (provider)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               1 ('packyapi')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               LOAD_ATTR                2 (auth_style)
    # |               STORE_FAST               5 (@py_assert7)
    # |               LOAD_CONST               2 ('bearer')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert10, @py_assert7)
    # |               LOAD_FAST_BORROW         6 (@py_assert10)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       265 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert9)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.provider\n}(%(py4)s)\n}.auth_style\n} == %(py11)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert7, @py_assert10)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('router')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('router')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py11')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert10)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format12)
    # |               LOAD_CONST              10 ('assert %(py13)s')
    # |               LOAD_CONST              11 ('py13')
    # |               LOAD_FAST_BORROW         8 (@py_format12)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format14)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format14)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  118 (@py_assert9, @py_assert10)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_native_anthropic_endpoint at 0x78a91fd400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 48>:
    # |  48           RESUME                   0
    # |  50           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                1 (provider + NULL|self)
    # |               LOAD_CONST               1 ('packyapi')
    # |               CALL                     1
    # |               STORE_FAST               2 (cfg)
    # |  51           LOAD_FAST_BORROW         2 (cfg)
    # |               LOAD_ATTR                2 (kind)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               2 ('anthropic')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py2)s\n{%(py2)s = %(py0)s.kind\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('cfg')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('cfg')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               7 ('assert %(py7)s')
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |  52           LOAD_FAST_BORROW         2 (cfg)
    # |               LOAD_ATTR               20 (base_url)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST              10 ('https://cf.api.fan')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.base_url\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('cfg')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('cfg')
    # |       L7:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               7 ('assert %(py7)s')
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_secret_read_from_env_not_hardcoded at 0x78a91fed00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 54>:
    # |  54           RESUME                   0
    # |  55           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                1 (provider + NULL|self)
    # |               LOAD_CONST               0 ('packyapi')
    # |               CALL                     1
    # |               STORE_FAST               2 (cfg)
    # |  56           LOAD_FAST_BORROW         2 (cfg)
    # |               LOAD_ATTR                2 (api_key_env)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               1 ('PACKYAPI_AUTH_TOKEN')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.api_key_env\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('cfg')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('cfg')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               6 ('assert %(py7)s')
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |  57           LOAD_GLOBAL             20 (CONFIG)
    # |               LOAD_ATTR               23 (read_text + NULL|self)
    # |               LOAD_CONST               9 ('utf-8')
    # |               CALL                     1
    # |               STORE_FAST               8 (raw)
    # |  58           LOAD_CONST              10 ('sk-')
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (raw)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       204 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              18 (('not in',))
    # |               LOAD_FAST_BORROW        10 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py1)s not in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (@py_assert0, raw)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              11 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py3')
    # |               LOAD_CONST              13 ('raw')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (raw)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (raw)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              13 ('raw')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format4)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 ('配置文件里出现了疑似密钥，密钥只能放 .env')
    # |               CALL                     1
    # |               LOAD_CONST              15 ('\n>assert %(py5)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               5 ('py5')
    # |               LOAD_FAST_BORROW        11 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_fallback_group_defined at 0x78a91ff200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 60>:
    # |  60           RESUME                   0
    # |  62           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                1 (provider + NULL|self)
    # |               LOAD_CONST               1 ('packyapi_awsq')
    # |               CALL                     1
    # |               STORE_FAST               2 (awsq)
    # |  63           LOAD_FAST_BORROW         2 (awsq)
    # |               LOAD_ATTR                2 (base_url)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               2 ('https://cf.api.fan')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py2)s\n{%(py2)s = %(py0)s.base_url\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('awsq')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (awsq)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (awsq)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('awsq')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               7 ('assert %(py7)s')
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |  64           LOAD_FAST_BORROW         2 (awsq)
    # |               LOAD_ATTR               20 (auth_style)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST              10 ('bearer')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.auth_style\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('awsq')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (awsq)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (awsq)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('awsq')
    # |       L7:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               7 ('assert %(py7)s')
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_awsq_retries_422 at 0x78a8e68a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 66>:
    # |  66           RESUME                   0
    # |  68           LOAD_CONST               1 (422)
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, router)
    # |               LOAD_ATTR                0 (provider)
    # |               STORE_FAST               3 (@py_assert4)
    # |               LOAD_CONST               2 ('packyapi_awsq')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert4)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert8, @py_assert8)
    # |               LOAD_ATTR                2 (retry_on_status)
    # |               STORE_FAST_LOAD_FAST    98 (@py_assert10, @py_assert0)
    # |               LOAD_FAST_BORROW         6 (@py_assert10)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       265 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('in',))
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s in %(py11)s\n{%(py11)s = %(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = %(py3)s.provider\n}(%(py7)s)\n}.retry_on_status\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 38 (@py_assert0, @py_assert10)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('router')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('router')
    # |       L3:     LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py11')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert10)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format12)
    # |               LOAD_CONST              10 ('assert %(py13)s')
    # |               LOAD_CONST              11 ('py13')
    # |               LOAD_FAST_BORROW         8 (@py_format12)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format14)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format14)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_retry_list_excludes_sdk_handled_codes at 0x78a9213900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 70>:
    # |   70            RESUME                   0
    # |   72            LOAD_FAST_BORROW         1 (router)
    # |                 LOAD_ATTR                1 (provider + NULL|self)
    # |                 LOAD_CONST               1 ('packyapi_awsq')
    # |                 CALL                     1
    # |                 LOAD_ATTR                2 (retry_on_status)
    # |                 STORE_FAST               2 (codes)
    # |   73            LOAD_FAST_BORROW         2 (codes)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      3 (c)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                13 (to L5)
    # |                 STORE_FAST_LOAD_FAST    51 (c, c)
    # |                 LOAD_CONST               7 ((408, 409, 429, 500, 503, 529))
    # |                 CONTAINS_OP              0 (in)
    # |         L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           11 (to L2)
    # |         L4:     LOAD_FAST_BORROW         3 (c)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           15 (to L2)
    # |         L5:     END_FOR
    # |                 POP_ITER
    # |         L6:     STORE_FAST               4 (overlap)
    # |                 STORE_FAST               3 (c)
    # |   74            LOAD_FAST_BORROW         4 (overlap)
    # |                 TO_BOOL
    # |                 UNARY_NOT
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       149 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              4 (@pytest_ar)
    # |                 LOAD_ATTR                6 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 ('这些码 SDK 已处理，不该再列：')
    # |                 LOAD_FAST_BORROW         4 (overlap)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 LOAD_CONST               3 ('\n>assert not %(py0)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               4 ('py0')
    # |                 LOAD_CONST               5 ('overlap')
    # |                 LOAD_GLOBAL              8 (@py_builtins)
    # |                 LOAD_ATTR               10 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              4 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (overlap)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |                 NOT_TAKEN
    # |         L7:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (overlap)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST               5 ('overlap')
    # |         L9:     BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format2)
    # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              4 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_format2)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST               6 (None)
    # |                 STORE_FAST               5 (@py_assert1)
    # |                 LOAD_CONST               6 (None)
    # |                 RETURN_VALUE
    # |   --   L11:     SWAP                     2
    # |                 POP_TOP
    # |   73            SWAP                     2
    # |                 STORE_FAST               3 (c)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L3 -> L11 [2]
    # |   L4 to L6 -> L11 [2]
    # | Disassembly of <code object test_primary_group_retries_transient_403 at 0x78a90c3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 76>:
    # |  76           RESUME                   0
    # |  81           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                1 (provider + NULL|self)
    # |               LOAD_CONST               1 ('packyapi')
    # |               CALL                     1
    # |               STORE_FAST               2 (cfg)
    # |  82           LOAD_CONST               2 (403)
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert0, cfg)
    # |               LOAD_ATTR                2 (retry_on_status)
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.retry_on_status\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('cfg')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('cfg')
    # |       L3:     LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_CONST               7 ('assert %(py7)s')
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert4)
    # |  83           LOAD_FAST_BORROW         2 (cfg)
    # |               LOAD_ATTR               20 (max_retries)
    # |               STORE_FAST               8 (@py_assert1)
    # |               LOAD_SMALL_INT           6
    # |               STORE_FAST_LOAD_FAST    72 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               COMPARE_OP             172 (>=)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       226 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('>=',))
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.max_retries\n} >= %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              10 ('py0')
    # |               LOAD_CONST               5 ('cfg')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (cfg)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               5 ('cfg')
    # |       L7:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 ('成功率低时重试次数太少等于没加')
    # |               CALL                     1
    # |               LOAD_CONST              13 ('\n>assert %(py7)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  148 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE

    def test_uses_bearer_not_x_api_key(self, router):
        '中转站要 Authorization: Bearer，官方才是 x-api-key。搞错必然 401。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  44           RESUME                   0
        # |  46           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                0 (provider)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               1 ('packyapi')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               LOAD_ATTR                2 (auth_style)
        # |               STORE_FAST               5 (@py_assert7)
        # |               LOAD_CONST               2 ('bearer')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert10, @py_assert7)
        # |               LOAD_FAST_BORROW         6 (@py_assert10)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       265 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert9)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.provider\n}(%(py4)s)\n}.auth_style\n} == %(py11)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert7, @py_assert10)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('router')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('router')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py11')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert10)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format12)
        # |               LOAD_CONST              10 ('assert %(py13)s')
        # |               LOAD_CONST              11 ('py13')
        # |               LOAD_FAST_BORROW         8 (@py_format12)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format14)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format14)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  118 (@py_assert9, @py_assert10)
        # |               LOAD_CONST              12 (None)
        # |               RETURN_VALUE

    def test_native_anthropic_endpoint(self, router):
        '必须走 anthropic 原生协议 —— cache_control 只在这条路上有效。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  48           RESUME                   0
        # |  50           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                1 (provider + NULL|self)
        # |               LOAD_CONST               1 ('packyapi')
        # |               CALL                     1
        # |               STORE_FAST               2 (cfg)
        # |  51           LOAD_FAST_BORROW         2 (cfg)
        # |               LOAD_ATTR                2 (kind)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               2 ('anthropic')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py2)s\n{%(py2)s = %(py0)s.kind\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('cfg')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('cfg')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               7 ('assert %(py7)s')
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |  52           LOAD_FAST_BORROW         2 (cfg)
        # |               LOAD_ATTR               20 (base_url)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST              10 ('https://cf.api.fan')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.base_url\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('cfg')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('cfg')
        # |       L7:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               7 ('assert %(py7)s')
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_secret_read_from_env_not_hardcoded(self, router):
        'packyapi'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  54           RESUME                   0
        # |  55           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                1 (provider + NULL|self)
        # |               LOAD_CONST               0 ('packyapi')
        # |               CALL                     1
        # |               STORE_FAST               2 (cfg)
        # |  56           LOAD_FAST_BORROW         2 (cfg)
        # |               LOAD_ATTR                2 (api_key_env)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               1 ('PACKYAPI_AUTH_TOKEN')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.api_key_env\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('cfg')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('cfg')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               6 ('assert %(py7)s')
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |  57           LOAD_GLOBAL             20 (CONFIG)
        # |               LOAD_ATTR               23 (read_text + NULL|self)
        # |               LOAD_CONST               9 ('utf-8')
        # |               CALL                     1
        # |               STORE_FAST               8 (raw)
        # |  58           LOAD_CONST              10 ('sk-')
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (raw)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       204 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              18 (('not in',))
        # |               LOAD_FAST_BORROW        10 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py1)s not in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (@py_assert0, raw)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              11 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py3')
        # |               LOAD_CONST              13 ('raw')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (raw)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (raw)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              13 ('raw')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format4)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 ('配置文件里出现了疑似密钥，密钥只能放 .env')
        # |               CALL                     1
        # |               LOAD_CONST              15 ('\n>assert %(py5)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               5 ('py5')
        # |               LOAD_FAST_BORROW        11 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_fallback_group_defined(self, router):
        'cc-sale 缓存异常时的退路必须配好，不用临时现查。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  60           RESUME                   0
        # |  62           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                1 (provider + NULL|self)
        # |               LOAD_CONST               1 ('packyapi_awsq')
        # |               CALL                     1
        # |               STORE_FAST               2 (awsq)
        # |  63           LOAD_FAST_BORROW         2 (awsq)
        # |               LOAD_ATTR                2 (base_url)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               2 ('https://cf.api.fan')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py2)s\n{%(py2)s = %(py0)s.base_url\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('awsq')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (awsq)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (awsq)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('awsq')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               7 ('assert %(py7)s')
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |  64           LOAD_FAST_BORROW         2 (awsq)
        # |               LOAD_ATTR               20 (auth_style)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST              10 ('bearer')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.auth_style\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('awsq')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (awsq)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (awsq)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('awsq')
        # |       L7:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               7 ('assert %(py7)s')
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_awsq_retries_422(self, router):
        'aws-q 官方警告"容易出现 422"，而 SDK 默认不重试 422。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  66           RESUME                   0
        # |  68           LOAD_CONST               1 (422)
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, router)
        # |               LOAD_ATTR                0 (provider)
        # |               STORE_FAST               3 (@py_assert4)
        # |               LOAD_CONST               2 ('packyapi_awsq')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert4)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert8, @py_assert8)
        # |               LOAD_ATTR                2 (retry_on_status)
        # |               STORE_FAST_LOAD_FAST    98 (@py_assert10, @py_assert0)
        # |               LOAD_FAST_BORROW         6 (@py_assert10)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       265 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('in',))
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s in %(py11)s\n{%(py11)s = %(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = %(py3)s.provider\n}(%(py7)s)\n}.retry_on_status\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 38 (@py_assert0, @py_assert10)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('router')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('router')
        # |       L3:     LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py11')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert10)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format12)
        # |               LOAD_CONST              10 ('assert %(py13)s')
        # |               LOAD_CONST              11 ('py13')
        # |               LOAD_FAST_BORROW         8 (@py_format12)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format14)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format14)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |               LOAD_CONST              12 (None)
        # |               RETURN_VALUE

    def test_retry_list_excludes_sdk_handled_codes(self, router):
        'SDK 已重试 408/409/429 与全部 5xx，重复列会导致乘法重试。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   70            RESUME                   0
        # |   72            LOAD_FAST_BORROW         1 (router)
        # |                 LOAD_ATTR                1 (provider + NULL|self)
        # |                 LOAD_CONST               1 ('packyapi_awsq')
        # |                 CALL                     1
        # |                 LOAD_ATTR                2 (retry_on_status)
        # |                 STORE_FAST               2 (codes)
        # |   73            LOAD_FAST_BORROW         2 (codes)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      3 (c)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                13 (to L5)
        # |                 STORE_FAST_LOAD_FAST    51 (c, c)
        # |                 LOAD_CONST               7 ((408, 409, 429, 500, 503, 529))
        # |                 CONTAINS_OP              0 (in)
        # |         L3:     POP_JUMP_IF_TRUE         3 (to L4)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           11 (to L2)
        # |         L4:     LOAD_FAST_BORROW         3 (c)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           15 (to L2)
        # |         L5:     END_FOR
        # |                 POP_ITER
        # |         L6:     STORE_FAST               4 (overlap)
        # |                 STORE_FAST               3 (c)
        # |   74            LOAD_FAST_BORROW         4 (overlap)
        # |                 TO_BOOL
        # |                 UNARY_NOT
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       149 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              4 (@pytest_ar)
        # |                 LOAD_ATTR                6 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 ('这些码 SDK 已处理，不该再列：')
        # |                 LOAD_FAST_BORROW         4 (overlap)
        # |                 FORMAT_SIMPLE
        # |                 BUILD_STRING             2
        # |                 CALL                     1
        # |                 LOAD_CONST               3 ('\n>assert not %(py0)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               4 ('py0')
        # |                 LOAD_CONST               5 ('overlap')
        # |                 LOAD_GLOBAL              8 (@py_builtins)
        # |                 LOAD_ATTR               10 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              4 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (overlap)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |                 NOT_TAKEN
        # |         L7:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (overlap)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST               5 ('overlap')
        # |         L9:     BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format2)
        # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              4 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_format2)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST               6 (None)
        # |                 STORE_FAST               5 (@py_assert1)
        # |                 LOAD_CONST               6 (None)
        # |                 RETURN_VALUE
        # |   --   L11:     SWAP                     2
        # |                 POP_TOP
        # |   73            SWAP                     2
        # |                 STORE_FAST               3 (c)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L3 -> L11 [2]
        # |   L4 to L6 -> L11 [2]

    def test_primary_group_retries_transient_403(self, router):
        '实测 cc-sale 号池会间歇性返回 403（上游账号失效的转述）。\n\nSDK 按语义把 403 当永久拒绝、不重试，所以必须显式加。\n'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  76           RESUME                   0
        # |  81           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                1 (provider + NULL|self)
        # |               LOAD_CONST               1 ('packyapi')
        # |               CALL                     1
        # |               STORE_FAST               2 (cfg)
        # |  82           LOAD_CONST               2 (403)
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert0, cfg)
        # |               LOAD_ATTR                2 (retry_on_status)
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.retry_on_status\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('cfg')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('cfg')
        # |       L3:     LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_CONST               7 ('assert %(py7)s')
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert4)
        # |  83           LOAD_FAST_BORROW         2 (cfg)
        # |               LOAD_ATTR               20 (max_retries)
        # |               STORE_FAST               8 (@py_assert1)
        # |               LOAD_SMALL_INT           6
        # |               STORE_FAST_LOAD_FAST    72 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               COMPARE_OP             172 (>=)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       226 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('>=',))
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.max_retries\n} >= %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 132 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              10 ('py0')
        # |               LOAD_CONST               5 ('cfg')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (cfg)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               5 ('cfg')
        # |       L7:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 ('成功率低时重试次数太少等于没加')
        # |               CALL                     1
        # |               LOAD_CONST              13 ('\n>assert %(py7)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  148 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE


class TestAuthStyle:
    'TestAuthStyle'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  86           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestAuthStyle')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          86
    # |               STORE_NAME               3 (__firstlineno__)
    # |  87           LOAD_CONST               1 (<code object __annotate__ at 0x1061324c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 87>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST               2 (<code object _client_kwargs at 0x1060434b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 87>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |               STORE_NAME               4 (_client_kwargs)
    # | 104           LOAD_CONST               3 (<code object test_bearer_uses_auth_token at 0x78a91ea300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 104>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_bearer_uses_auth_token)
    # | 109           LOAD_CONST               4 (<code object test_api_key_style_uses_api_key at 0x78a91e9900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 109>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_api_key_style_uses_api_key)
    # | 114           LOAD_CONST               5 (<code object test_base_url_forwarded at 0x78a91f0f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 114>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_base_url_forwarded)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x1061324c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 87>:
    # |  87           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('style')
    # |               LOAD_CONST               2 ('str')
    # |               LOAD_CONST               3 ('return')
    # |               LOAD_CONST               4 ('dict')
    # |               BUILD_MAP                2
    # |               RETURN_VALUE
    # | Disassembly of <code object _client_kwargs at 0x1060434b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 87>:
    # |   --           MAKE_CELL                5 (captured)
    # |   87           RESUME                   0
    # |   88           BUILD_MAP                0
    # |                STORE_DEREF              5 (captured)
    # |   90           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (captured)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               0 (<code object FakeAnthropic at 0x10610f330, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 90>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_CONST               1 ('FakeAnthropic')
    # |                CALL                     2
    # |                STORE_FAST               3 (FakeAnthropic)
    # |   94           LOAD_SMALL_INT           0
    # |                LOAD_CONST               2 (None)
    # |                IMPORT_NAME              0 (anthropic)
    # |                STORE_FAST               4 (anthropic)
    # |   96           LOAD_FAST_BORROW         1 (monkeypatch)
    # |                LOAD_ATTR                3 (setattr + NULL|self)
    # |                LOAD_FAST_BORROW         4 (anthropic)
    # |                LOAD_CONST               3 ('Anthropic')
    # |                LOAD_FAST_BORROW         3 (FakeAnthropic)
    # |                CALL                     3
    # |                POP_TOP
    # |   97           LOAD_FAST_BORROW         1 (monkeypatch)
    # |                LOAD_ATTR                5 (setenv + NULL|self)
    # |                LOAD_CONST               4 ('TEST_SECRET')
    # |                LOAD_CONST               5 ('sk-test-secret-value')
    # |                CALL                     2
    # |                POP_TOP
    # |   98           LOAD_GLOBAL              7 (AnthropicBackend + NULL)
    # |                LOAD_GLOBAL              9 (ProviderConfig + NULL)
    # |   99           LOAD_CONST               6 ('t')
    # |                LOAD_CONST               7 ('anthropic')
    # |                LOAD_CONST               4 ('TEST_SECRET')
    # |  100           LOAD_CONST               8 ('https://cf.api.fan')
    # |                LOAD_FAST_BORROW         2 (style)
    # |   98           LOAD_CONST               9 (('name', 'kind', 'api_key_env', 'base_url', 'auth_style'))
    # |                CALL_KW                  5
    # |                CALL                     1
    # |                POP_TOP
    # |  102           LOAD_DEREF               5 (captured)
    # |                RETURN_VALUE
    # | Disassembly of <code object FakeAnthropic at 0x10610f330, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 90>:
    # |   --           COPY_FREE_VARS           1
    # |   90           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('TestAuthStyle._client_kwargs.<locals>.FakeAnthropic')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT          90
    # |                STORE_NAME               3 (__firstlineno__)
    # |   91           LOAD_FAST_BORROW         0 (captured)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                STORE_NAME               4 (__init__)
    # |                LOAD_CONST               2 (())
    # |                STORE_NAME               5 (__static_attributes__)
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>:
    # |   --           COPY_FREE_VARS           1
    # |   91           RESUME                   0
    # |   92           LOAD_DEREF               2 (captured)
    # |                LOAD_ATTR                1 (update + NULL|self)
    # |                LOAD_FAST_BORROW         1 (kw)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_bearer_uses_auth_token at 0x78a91ea300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 104>:
    # | 104           RESUME                   0
    # | 105           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
    # |               LOAD_FAST_BORROW         1 (monkeypatch)
    # |               LOAD_CONST               0 ('bearer')
    # |               CALL                     2
    # |               STORE_FAST               2 (kw)
    # | 106           LOAD_FAST_BORROW         2 (kw)
    # |               LOAD_ATTR                2 (get)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               1 ('auth_token')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               5 (@py_assert5)
    # |               LOAD_CONST               2 ('sk-test-secret-value')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         6 (@py_assert8)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} == %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('kw')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('kw')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format10)
    # |               LOAD_CONST               9 ('assert %(py11)s')
    # |               LOAD_CONST              10 ('py11')
    # |               LOAD_FAST_BORROW         8 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format12)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  118 (@py_assert7, @py_assert8)
    # | 107           LOAD_CONST              12 ('api_key')
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 (('not in',))
    # |               LOAD_FAST_BORROW        11 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py1)s not in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (@py_assert0, kw)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              13 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py3')
    # |               LOAD_CONST               4 ('kw')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('kw')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format4)
    # |               LOAD_CONST              15 ('assert %(py5)s')
    # |               LOAD_CONST              16 ('py5')
    # |               LOAD_FAST_BORROW        12 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        13 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  171 (@py_assert0, @py_assert2)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_api_key_style_uses_api_key at 0x78a91e9900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 109>:
    # | 109           RESUME                   0
    # | 110           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
    # |               LOAD_FAST_BORROW         1 (monkeypatch)
    # |               LOAD_CONST               0 ('api_key')
    # |               CALL                     2
    # |               STORE_FAST               2 (kw)
    # | 111           LOAD_FAST_BORROW         2 (kw)
    # |               LOAD_ATTR                2 (get)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               0 ('api_key')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               5 (@py_assert5)
    # |               LOAD_CONST               1 ('sk-test-secret-value')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         6 (@py_assert8)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} == %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('kw')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('kw')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format10)
    # |               LOAD_CONST               8 ('assert %(py11)s')
    # |               LOAD_CONST               9 ('py11')
    # |               LOAD_FAST_BORROW         8 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format12)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  118 (@py_assert7, @py_assert8)
    # | 112           LOAD_CONST              11 ('auth_token')
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              18 (('not in',))
    # |               LOAD_FAST_BORROW        11 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py1)s not in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (@py_assert0, kw)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              12 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py3')
    # |               LOAD_CONST               3 ('kw')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (kw)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               3 ('kw')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format4)
    # |               LOAD_CONST              14 ('assert %(py5)s')
    # |               LOAD_CONST              15 ('py5')
    # |               LOAD_FAST_BORROW        12 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        13 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  171 (@py_assert0, @py_assert2)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_base_url_forwarded at 0x78a91f0f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 114>:
    # | 114           RESUME                   0
    # | 115           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
    # |               LOAD_FAST_BORROW         1 (monkeypatch)
    # |               LOAD_CONST               0 ('bearer')
    # |               CALL                     2
    # |               LOAD_CONST               1 ('base_url')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               2 ('https://cf.api.fan')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL              9 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE

    def _client_kwargs(self, monkeypatch, style):
        'FakeAnthropic'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                5 (captured)
        # |   87           RESUME                   0
        # |   88           BUILD_MAP                0
        # |                STORE_DEREF              5 (captured)
        # |   90           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (captured)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               0 (<code object FakeAnthropic at 0x10610f330, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 90>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_CONST               1 ('FakeAnthropic')
        # |                CALL                     2
        # |                STORE_FAST               3 (FakeAnthropic)
        # |   94           LOAD_SMALL_INT           0
        # |                LOAD_CONST               2 (None)
        # |                IMPORT_NAME              0 (anthropic)
        # |                STORE_FAST               4 (anthropic)
        # |   96           LOAD_FAST_BORROW         1 (monkeypatch)
        # |                LOAD_ATTR                3 (setattr + NULL|self)
        # |                LOAD_FAST_BORROW         4 (anthropic)
        # |                LOAD_CONST               3 ('Anthropic')
        # |                LOAD_FAST_BORROW         3 (FakeAnthropic)
        # |                CALL                     3
        # |                POP_TOP
        # |   97           LOAD_FAST_BORROW         1 (monkeypatch)
        # |                LOAD_ATTR                5 (setenv + NULL|self)
        # |                LOAD_CONST               4 ('TEST_SECRET')
        # |                LOAD_CONST               5 ('sk-test-secret-value')
        # |                CALL                     2
        # |                POP_TOP
        # |   98           LOAD_GLOBAL              7 (AnthropicBackend + NULL)
        # |                LOAD_GLOBAL              9 (ProviderConfig + NULL)
        # |   99           LOAD_CONST               6 ('t')
        # |                LOAD_CONST               7 ('anthropic')
        # |                LOAD_CONST               4 ('TEST_SECRET')
        # |  100           LOAD_CONST               8 ('https://cf.api.fan')
        # |                LOAD_FAST_BORROW         2 (style)
        # |   98           LOAD_CONST               9 (('name', 'kind', 'api_key_env', 'base_url', 'auth_style'))
        # |                CALL_KW                  5
        # |                CALL                     1
        # |                POP_TOP
        # |  102           LOAD_DEREF               5 (captured)
        # |                RETURN_VALUE
        # | Disassembly of <code object FakeAnthropic at 0x10610f330, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 90>:
        # |   --           COPY_FREE_VARS           1
        # |   90           RESUME                   0
        # |                LOAD_NAME                0 (__name__)
        # |                STORE_NAME               1 (__module__)
        # |                LOAD_CONST               0 ('TestAuthStyle._client_kwargs.<locals>.FakeAnthropic')
        # |                STORE_NAME               2 (__qualname__)
        # |                LOAD_SMALL_INT          90
        # |                STORE_NAME               3 (__firstlineno__)
        # |   91           LOAD_FAST_BORROW         0 (captured)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                STORE_NAME               4 (__init__)
        # |                LOAD_CONST               2 (())
        # |                STORE_NAME               5 (__static_attributes__)
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>:
        # |   --           COPY_FREE_VARS           1
        # |   91           RESUME                   0
        # |   92           LOAD_DEREF               2 (captured)
        # |                LOAD_ATTR                1 (update + NULL|self)
        # |                LOAD_FAST_BORROW         1 (kw)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE

        class FakeAnthropic:
            'TestAuthStyle._client_kwargs.<locals>.FakeAnthropic'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   90           RESUME                   0
            # |                LOAD_NAME                0 (__name__)
            # |                STORE_NAME               1 (__module__)
            # |                LOAD_CONST               0 ('TestAuthStyle._client_kwargs.<locals>.FakeAnthropic')
            # |                STORE_NAME               2 (__qualname__)
            # |                LOAD_SMALL_INT          90
            # |                STORE_NAME               3 (__firstlineno__)
            # |   91           LOAD_FAST_BORROW         0 (captured)
            # |                BUILD_TUPLE              1
            # |                LOAD_CONST               1 (<code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>)
            # |                MAKE_FUNCTION
            # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
            # |                STORE_NAME               4 (__init__)
            # |                LOAD_CONST               2 (())
            # |                STORE_NAME               5 (__static_attributes__)
            # |                LOAD_CONST               3 (None)
            # |                RETURN_VALUE
            # | Disassembly of <code object __init__ at 0x10610f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 91>:
            # |   --           COPY_FREE_VARS           1
            # |   91           RESUME                   0
            # |   92           LOAD_DEREF               2 (captured)
            # |                LOAD_ATTR                1 (update + NULL|self)
            # |                LOAD_FAST_BORROW         1 (kw)
            # |                CALL                     1
            # |                POP_TOP
            # |                LOAD_CONST               0 (None)
            # |                RETURN_VALUE

            def __init__(self, **kw):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # |   --           COPY_FREE_VARS           1
                # |   91           RESUME                   0
                # |   92           LOAD_DEREF               2 (captured)
                # |                LOAD_ATTR                1 (update + NULL|self)
                # |                LOAD_FAST_BORROW         1 (kw)
                # |                CALL                     1
                # |                POP_TOP
                # |                LOAD_CONST               0 (None)
                # |                RETURN_VALUE



    def test_bearer_uses_auth_token(self, monkeypatch):
        'bearer'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 104           RESUME                   0
        # | 105           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
        # |               LOAD_FAST_BORROW         1 (monkeypatch)
        # |               LOAD_CONST               0 ('bearer')
        # |               CALL                     2
        # |               STORE_FAST               2 (kw)
        # | 106           LOAD_FAST_BORROW         2 (kw)
        # |               LOAD_ATTR                2 (get)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               1 ('auth_token')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               5 (@py_assert5)
        # |               LOAD_CONST               2 ('sk-test-secret-value')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         6 (@py_assert8)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} == %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('kw')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('kw')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format10)
        # |               LOAD_CONST               9 ('assert %(py11)s')
        # |               LOAD_CONST              10 ('py11')
        # |               LOAD_FAST_BORROW         8 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format12)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  118 (@py_assert7, @py_assert8)
        # | 107           LOAD_CONST              12 ('api_key')
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 (('not in',))
        # |               LOAD_FAST_BORROW        11 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py1)s not in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (@py_assert0, kw)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              13 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py3')
        # |               LOAD_CONST               4 ('kw')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('kw')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format4)
        # |               LOAD_CONST              15 ('assert %(py5)s')
        # |               LOAD_CONST              16 ('py5')
        # |               LOAD_FAST_BORROW        12 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        13 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  171 (@py_assert0, @py_assert2)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_api_key_style_uses_api_key(self, monkeypatch):
        'api_key'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 109           RESUME                   0
        # | 110           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
        # |               LOAD_FAST_BORROW         1 (monkeypatch)
        # |               LOAD_CONST               0 ('api_key')
        # |               CALL                     2
        # |               STORE_FAST               2 (kw)
        # | 111           LOAD_FAST_BORROW         2 (kw)
        # |               LOAD_ATTR                2 (get)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               0 ('api_key')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               5 (@py_assert5)
        # |               LOAD_CONST               1 ('sk-test-secret-value')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         6 (@py_assert8)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} == %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('kw')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('kw')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format10)
        # |               LOAD_CONST               8 ('assert %(py11)s')
        # |               LOAD_CONST               9 ('py11')
        # |               LOAD_FAST_BORROW         8 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format12)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  118 (@py_assert7, @py_assert8)
        # | 112           LOAD_CONST              11 ('auth_token')
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST   187 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              18 (('not in',))
        # |               LOAD_FAST_BORROW        11 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py1)s not in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (@py_assert0, kw)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              12 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py3')
        # |               LOAD_CONST               3 ('kw')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (kw)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               3 ('kw')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format4)
        # |               LOAD_CONST              14 ('assert %(py5)s')
        # |               LOAD_CONST              15 ('py5')
        # |               LOAD_FAST_BORROW        12 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        13 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  171 (@py_assert0, @py_assert2)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_base_url_forwarded(self, monkeypatch):
        'bearer'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 114           RESUME                   0
        # | 115           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_client_kwargs + NULL|self)
        # |               LOAD_FAST_BORROW         1 (monkeypatch)
        # |               LOAD_CONST               0 ('bearer')
        # |               CALL                     2
        # |               LOAD_CONST               1 ('base_url')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               2 ('https://cf.api.fan')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL              9 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE


class TestNoSecretsInRepo:
    'TestNoSecretsInRepo'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 118           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestNoSecretsInRepo')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         118
    # |               STORE_NAME               3 (__firstlineno__)
    # | 119           LOAD_CONST               1 (<code object test_no_keys_committed at 0x78a91e8500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 119>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_no_keys_committed)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_no_keys_committed at 0x78a91e8500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 119>:
    # |   --            MAKE_CELL                8 (line)
    # |  119            RESUME                   0
    # |  121            LOAD_GLOBAL              0 (CONFIG)
    # |                 LOAD_ATTR                2 (parent)
    # |                 LOAD_ATTR                2 (parent)
    # |                 STORE_FAST               1 (root)
    # |  122            LOAD_GLOBAL              5 (list + NULL)
    # |                 LOAD_FAST_BORROW         1 (root)
    # |                 LOAD_ATTR                7 (glob + NULL|self)
    # |                 LOAD_CONST               1 ('config/*.yaml')
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 LOAD_FAST_BORROW         1 (root)
    # |                 LOAD_CONST               2 ('.env.example')
    # |                 BINARY_OP               11 (/)
    # |  123            LOAD_FAST_BORROW         1 (root)
    # |                 LOAD_CONST               3 ('README.md')
    # |                 BINARY_OP               11 (/)
    # |  122            BUILD_LIST               2
    # |                 BINARY_OP                0 (+)
    # |                 GET_ITER
    # |         L1:     EXTENDED_ARG             1
    # |                 FOR_ITER               365 (to L14)
    # |                 STORE_FAST               2 (path)
    # |  124            LOAD_FAST_BORROW         2 (path)
    # |                 LOAD_ATTR                9 (read_text + NULL|self)
    # |                 LOAD_CONST               4 ('utf-8')
    # |                 CALL                     1
    # |                 STORE_FAST               3 (text)
    # |  125            LOAD_GLOBAL             11 (enumerate + NULL)
    # |                 LOAD_FAST_BORROW         3 (text)
    # |                 LOAD_ATTR               13 (splitlines + NULL|self)
    # |                 CALL                     0
    # |                 LOAD_SMALL_INT           1
    # |                 CALL                     2
    # |                 GET_ITER
    # |         L2:     EXTENDED_ARG             1
    # |                 FOR_ITER               313 (to L13)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST               4 (n)
    # |                 STORE_DEREF              8 (line)
    # |  126            LOAD_CONST               5 ('sk-')
    # |                 LOAD_DEREF               8 (line)
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE         3 (to L3)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           16 (to L2)
    # |  127    L3:     LOAD_GLOBAL             14 (any)
    # |                 COPY                     1
    # |                 LOAD_COMMON_CONSTANT     4 (<built-in function any>)
    # |                 IS_OP                    0 (is)
    # |                 POP_JUMP_IF_FALSE       31 (to L7)
    # |                 NOT_TAKEN
    # |                 POP_TOP
    # |                 LOAD_FAST_BORROW         8 (line)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST               6 (<code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>)
    # |                 MAKE_FUNCTION
    # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |  128            LOAD_CONST              18 (('sk-...', 'sk-ant-...', '"sk-"', "'sk-'"))
    # |                 GET_ITER
    # |  127            CALL                     0
    # |         L4:     FOR_ITER                12 (to L6)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         3 (to L5)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           11 (to L4)
    # |         L5:     POP_ITER
    # |                 LOAD_CONST               7 (True)
    # |                 JUMP_FORWARD            20 (to L8)
    # |         L6:     END_FOR
    # |                 POP_ITER
    # |                 LOAD_CONST               8 (False)
    # |                 JUMP_FORWARD            16 (to L8)
    # |         L7:     PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (line)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST               6 (<code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>)
    # |                 MAKE_FUNCTION
    # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |  128            LOAD_CONST              18 (('sk-...', 'sk-ant-...', '"sk-"', "'sk-'"))
    # |                 GET_ITER
    # |  127            CALL                     0
    # |                 CALL                     1
    # |         L8:     STORE_FAST               5 (placeholder)
    # |  132            LOAD_DEREF               8 (line)
    # |                 LOAD_ATTR               17 (split + NULL|self)
    # |                 LOAD_CONST               9 ('=')
    # |                 CALL                     1
    # |                 LOAD_SMALL_INT           0
    # |                 BINARY_OP               26 ([])
    # |                 LOAD_ATTR               19 (strip + NULL|self)
    # |                 CALL                     0
    # |                 LOAD_ATTR               21 (lstrip + NULL|self)
    # |                 LOAD_CONST              10 ('#')
    # |                 CALL                     1
    # |                 LOAD_ATTR               19 (strip + NULL|self)
    # |                 CALL                     0
    # |                 STORE_FAST               6 (var)
    # |  133            LOAD_FAST_BORROW         5 (placeholder)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE        3 (to L9)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD          151 (to L2)
    # |         L9:     LOAD_GLOBAL             22 (@pytest_ar)
    # |  136            LOAD_ATTR               24 (_format_assertmsg)
    # |  133            PUSH_NULL
    # |  134            LOAD_FAST_BORROW         2 (path)
    # |                 LOAD_ATTR               26 (name)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              11 (':')
    # |                 LOAD_FAST_BORROW         4 (n)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              12 (' 变量 ')
    # |                 LOAD_FAST_BORROW         6 (var)
    # |                 CONVERT_VALUE            2 (repr)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              13 (' 疑似含真实密钥。真实密钥只能放 .env（已 gitignore），本文件只放占位符。')
    # |                 BUILD_STRING             6
    # |  133            CALL                     1
    # |                 LOAD_CONST              14 ('\n>assert %(py0)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              15 ('py0')
    # |                 LOAD_CONST              16 ('placeholder')
    # |                 LOAD_GLOBAL             28 (@py_builtins)
    # |  136            LOAD_ATTR               30 (locals)
    # |  133            PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |  136            LOAD_ATTR               32 (_should_repr_global_name)
    # |  133            PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (placeholder)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L11)
    # |                 NOT_TAKEN
    # |        L10:     LOAD_GLOBAL             22 (@pytest_ar)
    # |  136            LOAD_ATTR               34 (_saferepr)
    # |  133            PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (placeholder)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L12)
    # |        L11:     LOAD_CONST              16 ('placeholder')
    # |        L12:     BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format1)
    # |                 LOAD_GLOBAL             37 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |  136            LOAD_ATTR               38 (_format_explanation)
    # |  133            PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format1)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |  125   L13:     END_FOR
    # |                 POP_ITER
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD          368 (to L1)
    # |  122   L14:     END_FOR
    # |                 POP_ITER
    # |                 LOAD_CONST              17 (None)
    # |                 RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>:
    # |   --           COPY_FREE_VARS           1
    # |  127           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |  128   L2:     FOR_ITER                 9 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (t, t)
    # |                LOAD_DEREF               2 (line)
    # |                CONTAINS_OP              0 (in)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           11 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti

    def test_no_keys_committed(self):
        '密钥只能存在于 .env（已 gitignore）。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --            MAKE_CELL                8 (line)
        # |  119            RESUME                   0
        # |  121            LOAD_GLOBAL              0 (CONFIG)
        # |                 LOAD_ATTR                2 (parent)
        # |                 LOAD_ATTR                2 (parent)
        # |                 STORE_FAST               1 (root)
        # |  122            LOAD_GLOBAL              5 (list + NULL)
        # |                 LOAD_FAST_BORROW         1 (root)
        # |                 LOAD_ATTR                7 (glob + NULL|self)
        # |                 LOAD_CONST               1 ('config/*.yaml')
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 LOAD_FAST_BORROW         1 (root)
        # |                 LOAD_CONST               2 ('.env.example')
        # |                 BINARY_OP               11 (/)
        # |  123            LOAD_FAST_BORROW         1 (root)
        # |                 LOAD_CONST               3 ('README.md')
        # |                 BINARY_OP               11 (/)
        # |  122            BUILD_LIST               2
        # |                 BINARY_OP                0 (+)
        # |                 GET_ITER
        # |         L1:     EXTENDED_ARG             1
        # |                 FOR_ITER               365 (to L14)
        # |                 STORE_FAST               2 (path)
        # |  124            LOAD_FAST_BORROW         2 (path)
        # |                 LOAD_ATTR                9 (read_text + NULL|self)
        # |                 LOAD_CONST               4 ('utf-8')
        # |                 CALL                     1
        # |                 STORE_FAST               3 (text)
        # |  125            LOAD_GLOBAL             11 (enumerate + NULL)
        # |                 LOAD_FAST_BORROW         3 (text)
        # |                 LOAD_ATTR               13 (splitlines + NULL|self)
        # |                 CALL                     0
        # |                 LOAD_SMALL_INT           1
        # |                 CALL                     2
        # |                 GET_ITER
        # |         L2:     EXTENDED_ARG             1
        # |                 FOR_ITER               313 (to L13)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST               4 (n)
        # |                 STORE_DEREF              8 (line)
        # |  126            LOAD_CONST               5 ('sk-')
        # |                 LOAD_DEREF               8 (line)
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE         3 (to L3)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           16 (to L2)
        # |  127    L3:     LOAD_GLOBAL             14 (any)
        # |                 COPY                     1
        # |                 LOAD_COMMON_CONSTANT     4 (<built-in function any>)
        # |                 IS_OP                    0 (is)
        # |                 POP_JUMP_IF_FALSE       31 (to L7)
        # |                 NOT_TAKEN
        # |                 POP_TOP
        # |                 LOAD_FAST_BORROW         8 (line)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST               6 (<code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>)
        # |                 MAKE_FUNCTION
        # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |  128            LOAD_CONST              18 (('sk-...', 'sk-ant-...', '"sk-"', "'sk-'"))
        # |                 GET_ITER
        # |  127            CALL                     0
        # |         L4:     FOR_ITER                12 (to L6)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         3 (to L5)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           11 (to L4)
        # |         L5:     POP_ITER
        # |                 LOAD_CONST               7 (True)
        # |                 JUMP_FORWARD            20 (to L8)
        # |         L6:     END_FOR
        # |                 POP_ITER
        # |                 LOAD_CONST               8 (False)
        # |                 JUMP_FORWARD            16 (to L8)
        # |         L7:     PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (line)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST               6 (<code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>)
        # |                 MAKE_FUNCTION
        # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |  128            LOAD_CONST              18 (('sk-...', 'sk-ant-...', '"sk-"', "'sk-'"))
        # |                 GET_ITER
        # |  127            CALL                     0
        # |                 CALL                     1
        # |         L8:     STORE_FAST               5 (placeholder)
        # |  132            LOAD_DEREF               8 (line)
        # |                 LOAD_ATTR               17 (split + NULL|self)
        # |                 LOAD_CONST               9 ('=')
        # |                 CALL                     1
        # |                 LOAD_SMALL_INT           0
        # |                 BINARY_OP               26 ([])
        # |                 LOAD_ATTR               19 (strip + NULL|self)
        # |                 CALL                     0
        # |                 LOAD_ATTR               21 (lstrip + NULL|self)
        # |                 LOAD_CONST              10 ('#')
        # |                 CALL                     1
        # |                 LOAD_ATTR               19 (strip + NULL|self)
        # |                 CALL                     0
        # |                 STORE_FAST               6 (var)
        # |  133            LOAD_FAST_BORROW         5 (placeholder)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE        3 (to L9)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD          151 (to L2)
        # |         L9:     LOAD_GLOBAL             22 (@pytest_ar)
        # |  136            LOAD_ATTR               24 (_format_assertmsg)
        # |  133            PUSH_NULL
        # |  134            LOAD_FAST_BORROW         2 (path)
        # |                 LOAD_ATTR               26 (name)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST              11 (':')
        # |                 LOAD_FAST_BORROW         4 (n)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST              12 (' 变量 ')
        # |                 LOAD_FAST_BORROW         6 (var)
        # |                 CONVERT_VALUE            2 (repr)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST              13 (' 疑似含真实密钥。真实密钥只能放 .env（已 gitignore），本文件只放占位符。')
        # |                 BUILD_STRING             6
        # |  133            CALL                     1
        # |                 LOAD_CONST              14 ('\n>assert %(py0)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              15 ('py0')
        # |                 LOAD_CONST              16 ('placeholder')
        # |                 LOAD_GLOBAL             28 (@py_builtins)
        # |  136            LOAD_ATTR               30 (locals)
        # |  133            PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |  136            LOAD_ATTR               32 (_should_repr_global_name)
        # |  133            PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (placeholder)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L11)
        # |                 NOT_TAKEN
        # |        L10:     LOAD_GLOBAL             22 (@pytest_ar)
        # |  136            LOAD_ATTR               34 (_saferepr)
        # |  133            PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (placeholder)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L12)
        # |        L11:     LOAD_CONST              16 ('placeholder')
        # |        L12:     BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format1)
        # |                 LOAD_GLOBAL             37 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |  136            LOAD_ATTR               38 (_format_explanation)
        # |  133            PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format1)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |  125   L13:     END_FOR
        # |                 POP_ITER
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD          368 (to L1)
        # |  122   L14:     END_FOR
        # |                 POP_ITER
        # |                 LOAD_CONST              17 (None)
        # |                 RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x10610e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 127>:
        # |   --           COPY_FREE_VARS           1
        # |  127           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |  128   L2:     FOR_ITER                 9 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (t, t)
        # |                LOAD_DEREF               2 (line)
        # |                CONTAINS_OP              0 (in)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           11 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti


class TestFailoverChain:
    'TestFailoverChain'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 139           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestFailoverChain')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         139
    # |               STORE_NAME               3 (__firstlineno__)
    # | 140           LOAD_CONST               1 ('号池型渠道会整段时间不可用，重试再多也落在同一个坏窗口里。\n实测一次卷大纲把 9 次重试全用完仍然失败 —— 必须能换链路。')
    # |               STORE_NAME               4 (__doc__)
    # | 143           LOAD_CONST               2 (<code object test_creative_roles_have_fallbacks at 0x78a9217000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 143>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_creative_roles_have_fallbacks)
    # | 147           LOAD_CONST               3 (<code object test_prose_roles_use_one_model at 0x78a9217400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 147>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_prose_roles_use_one_model)
    # | 151           LOAD_CONST               4 (<code object test_writer_and_stitcher_share_the_fallback_chain at 0x78a9218500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 151>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_writer_and_stitcher_share_the_fallback_chain)
    # | 156           LOAD_CONST               5 (<code object test_codex_group_is_not_wired_to_any_role at 0x78a8e69180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 156>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_codex_group_is_not_wired_to_any_role)
    # | 164           LOAD_CONST               6 (<code object test_fallbacks_avoid_the_primary_pool at 0x78a921c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 164>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_fallbacks_avoid_the_primary_pool)
    # | 170           LOAD_CONST               7 (<code object test_every_creative_role_has_a_fallback at 0x78a9217800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 170>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_every_creative_role_has_a_fallback)
    # | 174           LOAD_CONST               8 (<code object test_fallback_providers_are_defined at 0x78a9217c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 174>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              11 (test_fallback_providers_are_defined)
    # | 179           LOAD_CONST               9 (<code object test_unknown_fallback_provider_fails_loudly at 0x78a91f1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 179>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              12 (test_unknown_fallback_provider_fails_loudly)
    # |               LOAD_CONST              10 (())
    # |               STORE_NAME              13 (__static_attributes__)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_creative_roles_have_fallbacks at 0x78a9217000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 143>:
    # | 143           RESUME                   0
    # | 144           LOAD_GLOBAL              0 (PROSE_ROLES)
    # |               GET_ITER
    # |       L1:     EXTENDED_ARG             1
    # |               FOR_ITER               339 (to L9)
    # |               STORE_FAST               2 (role)
    # | 145           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                2 (for_role)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |               LOAD_ATTR                4 (fallbacks)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       293 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               FORMAT_SIMPLE
    # |               LOAD_CONST               0 (' 没有降级链，主渠道挂了就整轮死')
    # |               BUILD_STRING             2
    # |               CALL                     1
    # |               LOAD_CONST               1 ('\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('router')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               3 ('router')
    # |       L4:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py3')
    # |               LOAD_CONST               6 ('role')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               6 ('role')
    # |       L7:     LOAD_CONST               7 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert4, @py_assert6)
    # |               EXTENDED_ARG             1
    # |               JUMP_BACKWARD          342 (to L1)
    # | 144   L9:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_prose_roles_use_one_model at 0x78a9217400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 147>:
    # |  147            RESUME                   0
    # |  148            LOAD_GLOBAL              0 (PROSE_ROLES)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      2 (r)
    # |                 SWAP                     2
    # |         L1:     BUILD_SET                0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                29 (to L3)
    # |                 STORE_FAST_LOAD_FAST    33 (r, router)
    # |                 LOAD_ATTR                3 (for_role + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (r)
    # |                 CALL                     1
    # |                 LOAD_ATTR                4 (model)
    # |                 SET_ADD                  2
    # |                 JUMP_BACKWARD           31 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               3 (models)
    # |                 STORE_FAST               2 (r)
    # |  149            LOAD_GLOBAL              7 (len + NULL)
    # |                 LOAD_FAST_BORROW         3 (models)
    # |                 CALL                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       315 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              11 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py0')
    # |                 LOAD_CONST               2 ('len')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               2 ('len')
    # |         L7:     LOAD_CONST               3 ('py1')
    # |                 LOAD_CONST               4 ('models')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (models)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (models)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               4 ('models')
    # |        L10:     LOAD_CONST               5 ('py3')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format7)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               7 ('创作链路用了多个模型：')
    # |                 LOAD_FAST_BORROW         3 (models)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('\n>assert %(py8)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               9 ('py8')
    # |                 LOAD_FAST_BORROW         7 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format9)
    # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST              10 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
    # |                 LOAD_CONST              10 (None)
    # |                 RETURN_VALUE
    # |   --   L12:     SWAP                     2
    # |                 POP_TOP
    # |  148            SWAP                     2
    # |                 STORE_FAST               2 (r)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L12 [2]
    # | Disassembly of <code object test_writer_and_stitcher_share_the_fallback_chain at 0x78a9218500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 151>:
    # | 151           RESUME                   0
    # | 154           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                0 (for_role)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               1 ('writer')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               LOAD_ATTR                2 (fallbacks)
    # |               STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
    # |               LOAD_ATTR                0 (for_role)
    # |               STORE_FAST               6 (@py_assert11)
    # |               LOAD_CONST               2 ('stitcher')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
    # |               LOAD_ATTR                2 (fallbacks)
    # |               STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
    # |               LOAD_FAST_BORROW         9 (@py_assert17)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       409 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW        10 (@py_assert9)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.fallbacks\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.fallbacks\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('router')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('router')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py10')
    # |               LOAD_CONST               4 ('router')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               4 ('router')
    # |       L6:     LOAD_CONST              10 ('py12')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py14')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py16')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert15)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py18')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert17)
    # |               CALL                     1
    # |               BUILD_MAP               10
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format19)
    # |               LOAD_CONST              14 ('assert %(py20)s')
    # |               LOAD_CONST              15 ('py20')
    # |               LOAD_FAST_BORROW        11 (@py_format19)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format21)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_format21)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              16 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST              10 (@py_assert9)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert11)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert13)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
    # |               LOAD_CONST              16 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_codex_group_is_not_wired_to_any_role at 0x78a8e69180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 156>:
    # |  156            RESUME                   0
    # |  159            LOAD_CONST               9 (('architect', 'writer', 'stitcher', 'judge', 'archivist', 'extractor'))
    # |                 GET_ITER
    # |         L1:     EXTENDED_ARG             1
    # |                 FOR_ITER               293 (to L10)
    # |                 STORE_FAST               2 (role)
    # |  160            LOAD_FAST_BORROW         1 (router)
    # |                 LOAD_ATTR                1 (for_role + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (role)
    # |                 CALL                     1
    # |                 STORE_FAST               3 (cfg)
    # |  161            LOAD_FAST_BORROW         3 (cfg)
    # |                 LOAD_ATTR                2 (provider)
    # |                 BUILD_LIST               1
    # |                 LOAD_FAST_BORROW         3 (cfg)
    # |                 LOAD_ATTR                4 (fallbacks)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      4 (p)
    # |                 LOAD_FAST_AND_CLEAR      5 (_)
    # |                 SWAP                     3
    # |         L2:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L3:     FOR_ITER                 7 (to L4)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   69 (p, _)
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD            9 (to L3)
    # |         L4:     END_FOR
    # |                 POP_ITER
    # |         L5:     SWAP                     3
    # |                 STORE_FAST               5 (_)
    # |                 STORE_FAST               4 (p)
    # |                 BINARY_OP                0 (+)
    # |                 STORE_FAST               6 (chain)
    # |  162            LOAD_CONST               1 ('packyapi_codex')
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert0, @py_assert0)
    # |                 LOAD_FAST_BORROW         6 (chain)
    # |                 CONTAINS_OP              1 (not in)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       207 (to L9)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR                8 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              10 (('not in',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              11 (('%(py1)s not in %(py3)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (@py_assert0, chain)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py1')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               3 ('py3')
    # |                 LOAD_CONST               4 ('chain')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L6)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (chain)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L7)
    # |                 NOT_TAKEN
    # |         L6:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (chain)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L8)
    # |         L7:     LOAD_CONST               4 ('chain')
    # |         L8:     BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format4)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (role)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST               5 (' 指向了被禁止的 codex 分组')
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('\n>assert %(py5)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               7 ('py5')
    # |                 LOAD_FAST_BORROW         9 (@py_format4)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format6)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format6)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L9:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  120 (@py_assert0, @py_assert2)
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD          296 (to L1)
    # |  159   L10:     END_FOR
    # |                 POP_ITER
    # |                 LOAD_CONST               8 (None)
    # |                 RETURN_VALUE
    # |   --   L11:     SWAP                     2
    # |                 POP_TOP
    # |  161            SWAP                     3
    # |                 STORE_FAST               5 (_)
    # |                 STORE_FAST               4 (p)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L2 to L5 -> L11 [5]
    # | Disassembly of <code object test_fallbacks_avoid_the_primary_pool at 0x78a921c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 164>:
    # |   --           MAKE_CELL                6 (cfg)
    # |  164           RESUME                   0
    # |  166           LOAD_GLOBAL              0 (PROSE_ROLES)
    # |                GET_ITER
    # |        L1:     FOR_ITER               233 (to L6)
    # |                STORE_FAST               2 (role)
    # |  167           LOAD_FAST_BORROW         1 (router)
    # |                LOAD_ATTR                3 (for_role + NULL|self)
    # |                LOAD_FAST_BORROW         2 (role)
    # |                CALL                     1
    # |                STORE_DEREF              6 (cfg)
    # |  168           LOAD_FAST_BORROW         6 (cfg)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object <genexpr> at 0x10612ee50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 168>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_DEREF               6 (cfg)
    # |                LOAD_ATTR                4 (fallbacks)
    # |                GET_ITER
    # |                CALL                     0
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_GLOBAL              7 (all + NULL)
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       171 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('all')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (all)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (all)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               4 ('all')
    # |        L4:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format5)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L5:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert3)
    # |                JUMP_BACKWARD          235 (to L1)
    # |  166   L6:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               7 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10612ee50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 168>:
    # |   --           COPY_FREE_VARS           1
    # |  168           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                22 (to L3)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   18 (p, _)
    # |                LOAD_FAST_BORROW         1 (p)
    # |                LOAD_DEREF               3 (cfg)
    # |                LOAD_ATTR                0 (provider)
    # |                COMPARE_OP             103 (!=)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           24 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_every_creative_role_has_a_fallback at 0x78a9217800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 170>:
    # | 170           RESUME                   0
    # | 171           LOAD_GLOBAL              0 (PROSE_ROLES)
    # |               GET_ITER
    # |       L1:     EXTENDED_ARG             1
    # |               FOR_ITER               339 (to L9)
    # |               STORE_FAST               2 (role)
    # | 172           LOAD_FAST_BORROW         1 (router)
    # |               LOAD_ATTR                2 (for_role)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |               LOAD_ATTR                4 (fallbacks)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       293 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               FORMAT_SIMPLE
    # |               LOAD_CONST               0 (' 没有降级链')
    # |               BUILD_STRING             2
    # |               CALL                     1
    # |               LOAD_CONST               1 ('\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('router')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (router)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               3 ('router')
    # |       L4:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py3')
    # |               LOAD_CONST               6 ('role')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (role)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               6 ('role')
    # |       L7:     LOAD_CONST               7 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert4, @py_assert6)
    # |               EXTENDED_ARG             1
    # |               JUMP_BACKWARD          342 (to L1)
    # | 171   L9:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_fallback_providers_are_defined at 0x78a9217c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 174>:
    # | 174            RESUME                   0
    # | 175            LOAD_GLOBAL              0 (PROSE_ROLES)
    # |                GET_ITER
    # |        L1:     EXTENDED_ARG             1
    # |                FOR_ITER               379 (to L11)
    # |                STORE_FAST               2 (role)
    # | 176            LOAD_FAST_BORROW         1 (router)
    # |                LOAD_ATTR                3 (for_role + NULL|self)
    # |                LOAD_FAST_BORROW         2 (role)
    # |                CALL                     1
    # |                LOAD_ATTR                4 (fallbacks)
    # |                GET_ITER
    # |        L2:     EXTENDED_ARG             1
    # |                FOR_ITER               343 (to L10)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (provider, _)
    # | 177            LOAD_FAST_BORROW         1 (router)
    # |                LOAD_ATTR                6 (provider)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (provider)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert4)
    # |                LOAD_CONST               0 (None)
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert7, @py_assert4)
    # |                LOAD_FAST_BORROW         7 (@py_assert7)
    # |                IS_OP                    1 (is not)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       299 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              10 (('is not',))
    # |                LOAD_FAST_BORROW         8 (@py_assert6)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              11 (('%(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.provider\n}(%(py3)s)\n} is not %(py8)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert4, @py_assert7)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('router')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L4)
    # |                NOT_TAKEN
    # |        L3:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (router)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L5)
    # |        L4:     LOAD_CONST               2 ('router')
    # |        L5:     LOAD_CONST               3 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('provider')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L6)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (provider)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L7)
    # |                NOT_TAKEN
    # |        L6:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (provider)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L8)
    # |        L7:     LOAD_CONST               5 ('provider')
    # |        L8:     LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py8')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert7)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format9)
    # |                LOAD_CONST               8 ('assert %(py10)s')
    # |                LOAD_CONST               9 ('py10')
    # |                LOAD_FAST_BORROW         9 (@py_format9)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format11)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format11)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L9:     LOAD_CONST               0 (None)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  135 (@py_assert6, @py_assert7)
    # |                EXTENDED_ARG             1
    # |                JUMP_BACKWARD          346 (to L2)
    # | 176   L10:     END_FOR
    # |                POP_ITER
    # |                EXTENDED_ARG             1
    # |                JUMP_BACKWARD          382 (to L1)
    # | 175   L11:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_unknown_fallback_provider_fails_loudly at 0x78a91f1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 179>:
    # |  179           RESUME                   0
    # |  180           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (yaml)
    # |                STORE_FAST               2 (yaml)
    # |  181           LOAD_SMALL_INT           0
    # |                LOAD_CONST               2 (('Router',))
    # |                IMPORT_NAME              1 (novel_agent.llm.router)
    # |                IMPORT_FROM              2 (Router)
    # |                STORE_FAST               3 (R)
    # |                POP_TOP
    # |  183           LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               3 ('m.yaml')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               4 (bad)
    # |  184           LOAD_FAST_BORROW         4 (bad)
    # |                LOAD_ATTR                7 (write_text + NULL|self)
    # |                LOAD_FAST_BORROW         2 (yaml)
    # |                LOAD_ATTR                9 (safe_dump + NULL|self)
    # |  185           LOAD_CONST               4 ('default_provider')
    # |                LOAD_CONST               5 ('a')
    # |  186           LOAD_CONST               6 ('providers')
    # |                LOAD_CONST               5 ('a')
    # |                LOAD_CONST               7 ('kind')
    # |                LOAD_CONST               8 ('anthropic')
    # |                LOAD_CONST               9 ('api_key_env')
    # |                LOAD_CONST              10 ('K')
    # |                BUILD_MAP                2
    # |                BUILD_MAP                1
    # |  187           LOAD_CONST              11 ('roles')
    # |                LOAD_CONST              12 ('writer')
    # |                LOAD_CONST              13 ('model')
    # |                LOAD_CONST              14 ('m')
    # |                LOAD_CONST              15 ('max_tokens')
    # |                LOAD_SMALL_INT          10
    # |  188           LOAD_CONST              16 ('fallbacks')
    # |                LOAD_CONST              17 ('provider')
    # |                LOAD_CONST              18 ('typo')
    # |                BUILD_MAP                1
    # |                BUILD_LIST               1
    # |  187           BUILD_MAP                3
    # |                BUILD_MAP                1
    # |  189           LOAD_CONST              19 ('cache_multipliers')
    # |                LOAD_CONST              20 ('read')
    # |                LOAD_CONST              21 (0.1)
    # |                LOAD_CONST              22 ('write_5m')
    # |                LOAD_CONST              23 (1.25)
    # |                LOAD_CONST              24 ('write_1h')
    # |                LOAD_CONST              25 (2.0)
    # |                BUILD_MAP                3
    # |  184           BUILD_MAP                4
    # |                CALL                     1
    # |  190           LOAD_CONST              26 ('utf-8')
    # |  184           CALL                     2
    # |                POP_TOP
    # |  191           LOAD_GLOBAL             10 (pytest)
    # |                LOAD_ATTR               12 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (ValueError)
    # |                LOAD_CONST              18 ('typo')
    # |                LOAD_CONST              27 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  192           LOAD_FAST_BORROW         3 (R)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (bad)
    # |                CALL                     1
    # |                POP_TOP
    # |  191   L2:     LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               1 (None)
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
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L6:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L3 [2] lasti
    # |   L3 to L5 -> L6 [4] lasti

    def test_creative_roles_have_fallbacks(self, router):
        ' 没有降级链，主渠道挂了就整轮死'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 143           RESUME                   0
        # | 144           LOAD_GLOBAL              0 (PROSE_ROLES)
        # |               GET_ITER
        # |       L1:     EXTENDED_ARG             1
        # |               FOR_ITER               339 (to L9)
        # |               STORE_FAST               2 (role)
        # | 145           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                2 (for_role)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |               LOAD_ATTR                4 (fallbacks)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       293 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               FORMAT_SIMPLE
        # |               LOAD_CONST               0 (' 没有降级链，主渠道挂了就整轮死')
        # |               BUILD_STRING             2
        # |               CALL                     1
        # |               LOAD_CONST               1 ('\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('router')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               3 ('router')
        # |       L4:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py3')
        # |               LOAD_CONST               6 ('role')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               6 ('role')
        # |       L7:     LOAD_CONST               7 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert4, @py_assert6)
        # |               EXTENDED_ARG             1
        # |               JUMP_BACKWARD          342 (to L1)
        # | 144   L9:     END_FOR
        # |               POP_ITER
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_prose_roles_use_one_model(self, router):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  147            RESUME                   0
        # |  148            LOAD_GLOBAL              0 (PROSE_ROLES)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      2 (r)
        # |                 SWAP                     2
        # |         L1:     BUILD_SET                0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                29 (to L3)
        # |                 STORE_FAST_LOAD_FAST    33 (r, router)
        # |                 LOAD_ATTR                3 (for_role + NULL|self)
        # |                 LOAD_FAST_BORROW         2 (r)
        # |                 CALL                     1
        # |                 LOAD_ATTR                4 (model)
        # |                 SET_ADD                  2
        # |                 JUMP_BACKWARD           31 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               3 (models)
        # |                 STORE_FAST               2 (r)
        # |  149            LOAD_GLOBAL              7 (len + NULL)
        # |                 LOAD_FAST_BORROW         3 (models)
        # |                 CALL                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       315 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              11 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py0')
        # |                 LOAD_CONST               2 ('len')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               2 ('len')
        # |         L7:     LOAD_CONST               3 ('py1')
        # |                 LOAD_CONST               4 ('models')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (models)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (models)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               4 ('models')
        # |        L10:     LOAD_CONST               5 ('py3')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format7)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               7 ('创作链路用了多个模型：')
        # |                 LOAD_FAST_BORROW         3 (models)
        # |                 FORMAT_SIMPLE
        # |                 BUILD_STRING             2
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('\n>assert %(py8)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               9 ('py8')
        # |                 LOAD_FAST_BORROW         7 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format9)
        # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST              10 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
        # |                 LOAD_CONST              10 (None)
        # |                 RETURN_VALUE
        # |   --   L12:     SWAP                     2
        # |                 POP_TOP
        # |  148            SWAP                     2
        # |                 STORE_FAST               2 (r)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L12 [2]

    def test_writer_and_stitcher_share_the_fallback_chain(self, router):
        '缝合与写作必须同进同退。若 writer 降级了而 stitcher 没有，\n同一章的正文和接缝就出自两支笔。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 151           RESUME                   0
        # | 154           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                0 (for_role)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               1 ('writer')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               LOAD_ATTR                2 (fallbacks)
        # |               STORE_FAST_LOAD_FAST    81 (@py_assert7, router)
        # |               LOAD_ATTR                0 (for_role)
        # |               STORE_FAST               6 (@py_assert11)
        # |               LOAD_CONST               2 ('stitcher')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert15, @py_assert15)
        # |               LOAD_ATTR                2 (fallbacks)
        # |               STORE_FAST_LOAD_FAST   149 (@py_assert17, @py_assert7)
        # |               LOAD_FAST_BORROW         9 (@py_assert17)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       409 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW        10 (@py_assert9)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py4)s)\n}.fallbacks\n} == %(py18)s\n{%(py18)s = %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.for_role\n}(%(py14)s)\n}.fallbacks\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (@py_assert7, @py_assert17)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('router')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('router')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py10')
        # |               LOAD_CONST               4 ('router')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               4 ('router')
        # |       L6:     LOAD_CONST              10 ('py12')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py14')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py16')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert15)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py18')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert17)
        # |               CALL                     1
        # |               BUILD_MAP               10
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format19)
        # |               LOAD_CONST              14 ('assert %(py20)s')
        # |               LOAD_CONST              15 ('py20')
        # |               LOAD_FAST_BORROW        11 (@py_format19)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format21)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_format21)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              16 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST              10 (@py_assert9)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert11)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert13)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  137 (@py_assert15, @py_assert17)
        # |               LOAD_CONST              16 (None)
        # |               RETURN_VALUE

    def test_codex_group_is_not_wired_to_any_role(self, router):
        'codex 分组明文禁止第三方接入并主动封锁非 Codex 客户端。\n实测 8 种协议/模型组合全被拒。配置保留只为记录，不能指过来。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  156            RESUME                   0
        # |  159            LOAD_CONST               9 (('architect', 'writer', 'stitcher', 'judge', 'archivist', 'extractor'))
        # |                 GET_ITER
        # |         L1:     EXTENDED_ARG             1
        # |                 FOR_ITER               293 (to L10)
        # |                 STORE_FAST               2 (role)
        # |  160            LOAD_FAST_BORROW         1 (router)
        # |                 LOAD_ATTR                1 (for_role + NULL|self)
        # |                 LOAD_FAST_BORROW         2 (role)
        # |                 CALL                     1
        # |                 STORE_FAST               3 (cfg)
        # |  161            LOAD_FAST_BORROW         3 (cfg)
        # |                 LOAD_ATTR                2 (provider)
        # |                 BUILD_LIST               1
        # |                 LOAD_FAST_BORROW         3 (cfg)
        # |                 LOAD_ATTR                4 (fallbacks)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      4 (p)
        # |                 LOAD_FAST_AND_CLEAR      5 (_)
        # |                 SWAP                     3
        # |         L2:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L3:     FOR_ITER                 7 (to L4)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST   69 (p, _)
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD            9 (to L3)
        # |         L4:     END_FOR
        # |                 POP_ITER
        # |         L5:     SWAP                     3
        # |                 STORE_FAST               5 (_)
        # |                 STORE_FAST               4 (p)
        # |                 BINARY_OP                0 (+)
        # |                 STORE_FAST               6 (chain)
        # |  162            LOAD_CONST               1 ('packyapi_codex')
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert0, @py_assert0)
        # |                 LOAD_FAST_BORROW         6 (chain)
        # |                 CONTAINS_OP              1 (not in)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       207 (to L9)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR                8 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              10 (('not in',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              11 (('%(py1)s not in %(py3)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (@py_assert0, chain)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py1')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               3 ('py3')
        # |                 LOAD_CONST               4 ('chain')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L6)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (chain)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L7)
        # |                 NOT_TAKEN
        # |         L6:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (chain)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L8)
        # |         L7:     LOAD_CONST               4 ('chain')
        # |         L8:     BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format4)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (role)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST               5 (' 指向了被禁止的 codex 分组')
        # |                 BUILD_STRING             2
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('\n>assert %(py5)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               7 ('py5')
        # |                 LOAD_FAST_BORROW         9 (@py_format4)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format6)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format6)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L9:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  120 (@py_assert0, @py_assert2)
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD          296 (to L1)
        # |  159   L10:     END_FOR
        # |                 POP_ITER
        # |                 LOAD_CONST               8 (None)
        # |                 RETURN_VALUE
        # |   --   L11:     SWAP                     2
        # |                 POP_TOP
        # |  161            SWAP                     3
        # |                 STORE_FAST               5 (_)
        # |                 STORE_FAST               4 (p)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L2 to L5 -> L11 [5]

    def test_fallbacks_avoid_the_primary_pool(self, router):
        '降级目标不能和主渠道是同一个池子 —— 那等于没降级。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                6 (cfg)
        # |  164           RESUME                   0
        # |  166           LOAD_GLOBAL              0 (PROSE_ROLES)
        # |                GET_ITER
        # |        L1:     FOR_ITER               233 (to L6)
        # |                STORE_FAST               2 (role)
        # |  167           LOAD_FAST_BORROW         1 (router)
        # |                LOAD_ATTR                3 (for_role + NULL|self)
        # |                LOAD_FAST_BORROW         2 (role)
        # |                CALL                     1
        # |                STORE_DEREF              6 (cfg)
        # |  168           LOAD_FAST_BORROW         6 (cfg)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object <genexpr> at 0x10612ee50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 168>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_DEREF               6 (cfg)
        # |                LOAD_ATTR                4 (fallbacks)
        # |                GET_ITER
        # |                CALL                     0
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_GLOBAL              7 (all + NULL)
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       171 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('all')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (all)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (all)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               4 ('all')
        # |        L4:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format5)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L5:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert3)
        # |                JUMP_BACKWARD          235 (to L1)
        # |  166   L6:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               7 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x10612ee50, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_config_wiring.py", line 168>:
        # |   --           COPY_FREE_VARS           1
        # |  168           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                22 (to L3)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   18 (p, _)
        # |                LOAD_FAST_BORROW         1 (p)
        # |                LOAD_DEREF               3 (cfg)
        # |                LOAD_ATTR                0 (provider)
        # |                COMPARE_OP             103 (!=)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           24 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_every_creative_role_has_a_fallback(self, router):
        ' 没有降级链'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 170           RESUME                   0
        # | 171           LOAD_GLOBAL              0 (PROSE_ROLES)
        # |               GET_ITER
        # |       L1:     EXTENDED_ARG             1
        # |               FOR_ITER               339 (to L9)
        # |               STORE_FAST               2 (role)
        # | 172           LOAD_FAST_BORROW         1 (router)
        # |               LOAD_ATTR                2 (for_role)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |               LOAD_ATTR                4 (fallbacks)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       293 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               FORMAT_SIMPLE
        # |               LOAD_CONST               0 (' 没有降级链')
        # |               BUILD_STRING             2
        # |               CALL                     1
        # |               LOAD_CONST               1 ('\n>assert %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.for_role\n}(%(py3)s)\n}.fallbacks\n}')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('router')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (router)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               3 ('router')
        # |       L4:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py3')
        # |               LOAD_CONST               6 ('role')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (role)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               6 ('role')
        # |       L7:     LOAD_CONST               7 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert4, @py_assert6)
        # |               EXTENDED_ARG             1
        # |               JUMP_BACKWARD          342 (to L1)
        # | 171   L9:     END_FOR
        # |               POP_ITER
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_fallback_providers_are_defined(self, router):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 174            RESUME                   0
        # | 175            LOAD_GLOBAL              0 (PROSE_ROLES)
        # |                GET_ITER
        # |        L1:     EXTENDED_ARG             1
        # |                FOR_ITER               379 (to L11)
        # |                STORE_FAST               2 (role)
        # | 176            LOAD_FAST_BORROW         1 (router)
        # |                LOAD_ATTR                3 (for_role + NULL|self)
        # |                LOAD_FAST_BORROW         2 (role)
        # |                CALL                     1
        # |                LOAD_ATTR                4 (fallbacks)
        # |                GET_ITER
        # |        L2:     EXTENDED_ARG             1
        # |                FOR_ITER               343 (to L10)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (provider, _)
        # | 177            LOAD_FAST_BORROW         1 (router)
        # |                LOAD_ATTR                6 (provider)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (provider)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert4)
        # |                LOAD_CONST               0 (None)
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert7, @py_assert4)
        # |                LOAD_FAST_BORROW         7 (@py_assert7)
        # |                IS_OP                    1 (is not)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert6, @py_assert6)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       299 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              10 (('is not',))
        # |                LOAD_FAST_BORROW         8 (@py_assert6)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              11 (('%(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.provider\n}(%(py3)s)\n} is not %(py8)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert4, @py_assert7)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('router')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L3)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L4)
        # |                NOT_TAKEN
        # |        L3:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (router)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L5)
        # |        L4:     LOAD_CONST               2 ('router')
        # |        L5:     LOAD_CONST               3 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('provider')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L6)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (provider)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L7)
        # |                NOT_TAKEN
        # |        L6:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (provider)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L8)
        # |        L7:     LOAD_CONST               5 ('provider')
        # |        L8:     LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py8')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert7)
        # |                CALL                     1
        # |                BUILD_MAP                5
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format9)
        # |                LOAD_CONST               8 ('assert %(py10)s')
        # |                LOAD_CONST               9 ('py10')
        # |                LOAD_FAST_BORROW         9 (@py_format9)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format11)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format11)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L9:     LOAD_CONST               0 (None)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  135 (@py_assert6, @py_assert7)
        # |                EXTENDED_ARG             1
        # |                JUMP_BACKWARD          346 (to L2)
        # | 176   L10:     END_FOR
        # |                POP_ITER
        # |                EXTENDED_ARG             1
        # |                JUMP_BACKWARD          382 (to L1)
        # | 175   L11:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE

    def test_unknown_fallback_provider_fails_loudly(self, tmp_path):
        'm.yaml'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  179           RESUME                   0
        # |  180           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (yaml)
        # |                STORE_FAST               2 (yaml)
        # |  181           LOAD_SMALL_INT           0
        # |                LOAD_CONST               2 (('Router',))
        # |                IMPORT_NAME              1 (novel_agent.llm.router)
        # |                IMPORT_FROM              2 (Router)
        # |                STORE_FAST               3 (R)
        # |                POP_TOP
        # |  183           LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               3 ('m.yaml')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               4 (bad)
        # |  184           LOAD_FAST_BORROW         4 (bad)
        # |                LOAD_ATTR                7 (write_text + NULL|self)
        # |                LOAD_FAST_BORROW         2 (yaml)
        # |                LOAD_ATTR                9 (safe_dump + NULL|self)
        # |  185           LOAD_CONST               4 ('default_provider')
        # |                LOAD_CONST               5 ('a')
        # |  186           LOAD_CONST               6 ('providers')
        # |                LOAD_CONST               5 ('a')
        # |                LOAD_CONST               7 ('kind')
        # |                LOAD_CONST               8 ('anthropic')
        # |                LOAD_CONST               9 ('api_key_env')
        # |                LOAD_CONST              10 ('K')
        # |                BUILD_MAP                2
        # |                BUILD_MAP                1
        # |  187           LOAD_CONST              11 ('roles')
        # |                LOAD_CONST              12 ('writer')
        # |                LOAD_CONST              13 ('model')
        # |                LOAD_CONST              14 ('m')
        # |                LOAD_CONST              15 ('max_tokens')
        # |                LOAD_SMALL_INT          10
        # |  188           LOAD_CONST              16 ('fallbacks')
        # |                LOAD_CONST              17 ('provider')
        # |                LOAD_CONST              18 ('typo')
        # |                BUILD_MAP                1
        # |                BUILD_LIST               1
        # |  187           BUILD_MAP                3
        # |                BUILD_MAP                1
        # |  189           LOAD_CONST              19 ('cache_multipliers')
        # |                LOAD_CONST              20 ('read')
        # |                LOAD_CONST              21 (0.1)
        # |                LOAD_CONST              22 ('write_5m')
        # |                LOAD_CONST              23 (1.25)
        # |                LOAD_CONST              24 ('write_1h')
        # |                LOAD_CONST              25 (2.0)
        # |                BUILD_MAP                3
        # |  184           BUILD_MAP                4
        # |                CALL                     1
        # |  190           LOAD_CONST              26 ('utf-8')
        # |  184           CALL                     2
        # |                POP_TOP
        # |  191           LOAD_GLOBAL             10 (pytest)
        # |                LOAD_ATTR               12 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (ValueError)
        # |                LOAD_CONST              18 ('typo')
        # |                LOAD_CONST              27 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  192           LOAD_FAST_BORROW         3 (R)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (bad)
        # |                CALL                     1
        # |                POP_TOP
        # |  191   L2:     LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               1 (None)
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
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L6:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L3 [2] lasti
        # |   L3 to L5 -> L6 [4] lasti

