from ariadne import ObjectType, convert_kwargs_to_snake_case
from ...business.algo import Algo
from ...utils import map_resolver

query = ObjectType("Query")


@query.field("getAlgorithms")
def get_algorithms(_, info):
    algo = Algo(info.context)
    return algo.get_algorithms()


resolvers = [query]
