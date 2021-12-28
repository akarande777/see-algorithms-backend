from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers
from .resolvers import auth

type_defs = load_schema_from_path("src/graphql/schema/")

resolvers = [*auth.resolvers]

schema = make_executable_schema(
    type_defs, *resolvers, snake_case_fallback_resolvers)
