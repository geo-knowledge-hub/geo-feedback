# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Group on Earth Observations (GEO).
#
# geo-feedback is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from flask_babelex import gettext as _
from invenio_records_resources.services.records.facets import TermsFacet

#
# Status Facet
#
status = TermsFacet(field="status", label=_("Status"))

#
# Record Facet
#
record = TermsFacet(field="record", label=_("Record"))
