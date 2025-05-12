# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018, 2020, 2021 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Workflow-Engine-CWL tests."""

from __future__ import absolute_import, print_function


def test_version():
    """Test version import."""
    from reana_workflow_engine_cwl import __version__

    assert __version__
