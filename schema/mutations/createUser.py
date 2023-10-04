#!/usr/bin/env python3
"""Handles user creation"""

import graphene
from models.user import User as UserModel
from models import storage
from flask import g
from models.roles import UserRole
from schema.models import User


class CreateUser(graphene.Mutation):
    """Handles user creation"""
    class Arguments:
        """Defines arguments for creating a user"""
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        firstname = graphene.String(required=False)
        lastname = graphene.String(required=False)

    user = graphene.Field(lambda: User)

    def mutate(root, info, username, email, password, firstname="", lastname=""):
        """Creates a new user in the database"""
        user = UserModel(
            username=username,
            email=email,
            _password=password,
            firstname=firstname,
            lastname=lastname
        )

        storage.new(user)
        storage.save()

        return CreateUser(user=user)