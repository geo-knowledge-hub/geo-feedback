# -*- coding: utf-8 -*-
#
# This file is part of GEO Knowledge Hub User's Feedback Component.
# Copyright 2021 GEO Secretariat.
#
# GEO Knowledge Hub User's Feedback Component is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from invenio_records.dictutils import dict_lookup

from invenio_accounts.models import User as InvenioUser
from invenio_rdm_records.records.api import RDMRecord


class EntityBase:
    """Base entity abstraction class."""

    entity_cls = None

    def __init__(self, entity=None):
        """Initializer.

        Args:
            entity (object): Entity object.
        """
        self._entity = entity

    @classmethod
    def from_object(cls, instance):
        """Create a new Entity object from a record instance object.

        Note:
            This method must be overwritten by subclasses.
        """
        pass

    def dump(self):
        """Dump the entity object into a dict.

        Note:
            This method must be overwritten by subclasses.
        """
        pass

    def resolve(self):
        """Resolve the entity object."""
        return self._entity


class UserEntity(EntityBase):
    """User entity abstraction class."""

    entity_cls = InvenioUser

    @classmethod
    def from_object(cls, instance):
        if type(instance) == dict:
            user_id = dict_lookup(instance, "user_id")

        else:
            # note: assuming the instance model class
            # (in this case `FeedbackRecord`).
            user_id = getattr(instance.model, "user_id")

        return (
            cls(
                entity=InvenioUser.query.get(user_id),
            )
            if user_id
            else None
        )

    def dump(self):
        return {"user_id": self._entity.id}


class RecordEntity(EntityBase):
    """Record entity abstraction class."""

    entity_cls = RDMRecord

    @classmethod
    def from_object(cls, instance):

        if type(instance) == dict:
            record_pid = dict_lookup(instance, "record_pid")
            obj = RDMRecord.pid.resolve(record_pid)

        else:
            # note: assuming the instance model class
            # (in this case `FeedbackRecord`).
            record_id = getattr(instance.model, "record_id")
            obj = RDMRecord.get_record(record_id)

        return (
            cls(
                entity=obj,
            )
            if record_id
            else None
        )

    def dump(self):
        return {"record_pid": self._entity.pid.pid_value}
