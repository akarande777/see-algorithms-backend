from ariadne import ObjectType, convert_kwargs_to_snake_case
from ...business.auth import Auth
from ...utils import auth_token, map_resolver

mutation = ObjectType("Mutation")
user_auth = ObjectType("UserAuth")


@mutation.field("login")
@convert_kwargs_to_snake_case
def login(_, info, **args):
    auth = Auth(info.context)
    return auth.login(**args)


@mutation.field("register")
@convert_kwargs_to_snake_case
def register(_, info, **args):
    auth = Auth(info.context)
    return auth.register(**args)


@mutation.field("confirmEmail")
@convert_kwargs_to_snake_case
def confirm_email(_, info, token):
    auth = Auth(info.context)
    return auth.confirm_email(token)


map_resolver(user_auth, {
    "authToken": lambda obj, _: auth_token(obj.user_id),
})

resolvers = [mutation, user_auth]
