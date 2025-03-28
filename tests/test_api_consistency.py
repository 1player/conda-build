# Copyright (C) 2014 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
# This file makes sure that our API has not changed.  Doing so can not be accidental.  Whenever it
#    happens, we should bump our major build number, because we may have broken someone.

import sys

import pytest

from conda_build import api

from inspect import getfullargspec as getargspec

pytestmark = pytest.mark.no_default_testing_config


def test_api_config():
    assert hasattr(api, 'Config')
    assert hasattr(api, 'get_or_merge_config')


def test_api_get_or_merge_config():
    argspec = getargspec(api.get_or_merge_config)
    assert argspec.args == ['config', 'variant']
    assert argspec.defaults == (None, )


def test_api_render():
    argspec = getargspec(api.render)
    assert argspec.args == ['recipe_path', 'config', 'variants',
                            'permit_unsatisfiable_variants', 'finalize',
                            'bypass_env_check']
    assert argspec.defaults == (None, None, True, True, False)


def test_api_output_yaml():
    argspec = getargspec(api.output_yaml)
    assert argspec.args == ['metadata', 'file_path', 'suppress_outputs']
    assert argspec.defaults == (None, False)


def test_api_get_output_file_path():
    argspec = getargspec(api.get_output_file_path)
    assert argspec.args == ['recipe_path_or_metadata', 'no_download_source', 'config', 'variants']
    assert argspec.defaults == (False, None, None)


def test_api_check():
    argspec = getargspec(api.check)
    assert argspec.args == ['recipe_path', 'no_download_source', 'config', 'variants']
    assert argspec.defaults == (False, None, None)


def test_api_build():
    argspec = getargspec(api.build)
    assert argspec.args == ['recipe_paths_or_metadata', 'post', 'need_source_download',
                            'build_only', 'notest', 'config', 'variants', 'stats']
    assert argspec.defaults == (None, True, False, False, None, None, None)


def test_api_test():
    argspec = getargspec(api.test)
    assert argspec.args == ['recipedir_or_package_or_metadata', 'move_broken', 'config', 'stats']
    assert argspec.defaults == (True, None, None)


def test_api_list_skeletons():
    argspec = getargspec(api.list_skeletons)
    assert argspec.args == []
    assert argspec.defaults is None


def test_api_skeletonize():
    argspec = getargspec(api.skeletonize)
    assert argspec.args == ['packages', 'repo', 'output_dir', 'version', 'recursive', 'config']
    assert argspec.defaults == ('.', None, False, None)


def test_api_develop():
    argspec = getargspec(api.develop)
    assert argspec.args == ['recipe_dir', 'prefix', 'no_pth_file', 'build_ext',
                            'clean', 'uninstall']
    assert argspec.defaults == (sys.prefix, False, False, False, False)


def test_api_convert():
    argspec = getargspec(api.convert)
    assert argspec.args == ['package_file', 'output_dir', 'show_imports', 'platforms', 'force',
                            'dependencies', 'verbose', 'quiet', 'dry_run']
    assert argspec.defaults == ('.', False, None, False, None, False, True, False)


def test_api_installable():
    argspec = getargspec(api.test_installable)
    assert argspec.args == ['channel']
    assert argspec.defaults == ('defaults',)


def test_api_inspect_linkages():
    argspec = getargspec(api.inspect_linkages)
    assert argspec.args == ['packages', 'prefix', 'untracked', 'all_packages',
                            'show_files', 'groupby', 'sysroot']
    assert argspec.defaults == (sys.prefix, False, False, False, 'package', '')


def test_api_inspect_objects():
    argspec = getargspec(api.inspect_objects)
    assert argspec.args == ['packages', 'prefix', 'groupby']
    assert argspec.defaults == (sys.prefix, 'filename')


def test_api_inspect_prefix_length():
    argspec = getargspec(api.inspect_prefix_length)
    assert argspec.args == ['packages', 'min_prefix_length']
    # hard-coded prefix length as intentional check here
    assert argspec.defaults == (255,)


def test_api_create_metapackage():
    argspec = getargspec(api.create_metapackage)
    assert argspec.args == ['name', 'version', 'entry_points', 'build_string', 'build_number',
                            'dependencies', 'home', 'license_name', 'summary', 'config']
    assert argspec.defaults == ((), None, 0, (), None, None, None, None)


def test_api_update_index():
    argspec = getargspec(api.update_index)
    assert argspec.args == ['dir_paths', 'config', 'force', 'check_md5', 'remove', 'channel_name', 'subdir',
                            'threads', 'patch_generator', "verbose", "progress", "hotfix_source_repo",
                            'current_index_versions']
    assert argspec.defaults == (None, False, False, False, None, None, None, None, False, False, None, None)
