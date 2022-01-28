# import graphene
# import graphene_django_cud.mutations as django_cud_mutations
# import graphene_django_optimizer as gql_optimizer
# import inflection
# from django_filters.filterset import FilterSet
# from graphene_django.filter.utils import get_filtering_args_from_filterset
#
# import starwars.models as starwars_models
#
# ALL_MODELS = [*(map(starwars_models.__dict__.get, starwars_models.__all__))]
#
#
# def queries(model):
#     model_name = model.__name__
#     underscore_name = inflection.underscore(model_name)
#     plural_underscore_name = inflection.pluralize(underscore_name)
#     object_type = type(
#         f"{model_name}ObjectType",
#         (gql_optimizer.OptimizedDjangoObjectType,),
#         {"Meta": type("Meta", (object,), {"model": model})},
#     )
#
#     def list_resolver(root, info, offset=None, limit=None, **filters):
#         qs = model.objects.filter(**filters).all()
#         if offset is not None:
#             qs = qs[offset:]
#         if limit is not None:
#             qs = qs[:limit]
#         return gql_optimizer.query(
#             qs,
#             info,
#         )
#
#     filtering_args = get_filtering_args_from_filterset(
#         type(
#             f"{model_name}FilterSet",
#             (FilterSet,),
#             {
#                 "Meta": type("Meta", (object,), {"model": model, "exclude": []}),
#             },
#         ),
#         object_type,
#     )
#
#     return type(
#         f"{model_name}Query",
#         (graphene.ObjectType,),
#         {
#             f"{underscore_name}": graphene.Field(object_type, id=graphene.ID()),
#             f"{plural_underscore_name}": graphene.List(
#                 object_type,
#                 offset=graphene.Int(),
#                 limit=graphene.Int(),
#                 **filtering_args,
#             ),
#             f"resolve_{plural_underscore_name}": list_resolver,
#         },
#     )
#
#
# def mutations(model):
#     model_name = model.__name__
#     underscore_name = inflection.underscore(model_name)
#
#     create_mutation = type(
#         f"Create{model_name}Mutation",
#         (django_cud_mutations.DjangoCreateMutation,),
#         {"Meta": type("Meta", (object,), {"model": model})},
#     )
#
#     update_mutation = type(
#         f"Update{model_name}Mutation",
#         (django_cud_mutations.DjangoUpdateMutation,),
#         {"Meta": type("Meta", (object,), {"model": model})},
#     )
#
#     delete_mutation = type(
#         f"Delete{model_name}Mutation",
#         (django_cud_mutations.DjangoDeleteMutation,),
#         {"Meta": type("Meta", (object,), {"model": model})},
#     )
#
#     return type(
#         f"{model_name}Mutation",
#         (graphene.ObjectType,),
#         {
#             f"create_{underscore_name}": create_mutation.Field(),
#             f"update_{underscore_name}": update_mutation.Field(),
#             f"delete_{underscore_name}": delete_mutation.Field(),
#         },
#     )
#
#
# schema = graphene.Schema(
#     query=type(
#         "Query",
#         (*[queries(model) for model in ALL_MODELS],) + (graphene.ObjectType,),
#         {},
#     ),
#     mutation=type(
#         "Mutation",
#         (*[mutations(model) for model in ALL_MODELS],) + (graphene.ObjectType,),
#         {},
#     ),
# )
#

import graphene
import graphene_django_cud.mutations as django_cud_mutations
import inflection
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from starwars import models

ALL_MODELS = [*(map(models.__dict__.get, models.__all__))]


def queries(model):
    model_name = model.__name__
    underscore_name = inflection.underscore(model_name)
    plural_underscore_name = inflection.pluralize(underscore_name)
    object_type = type(
        f"{model_name}",
        (DjangoObjectType,),
        {"Meta": type("Meta", (object,), {"model": model})},
    )

    def get_resolver(root, info, id):

        try:
            return model.objects.get(pk=id)
        except Exception as errors:
            return errors

    def list_resolver(root, info):
        return model.objects.all()

    return type(
        f"{model_name}Query",
        (graphene.ObjectType,),
        {
            f"{underscore_name}": graphene.Field(object_type, id=graphene.UUID()),
            f"{plural_underscore_name}": graphene.List(object_type),
            f"resolve_{underscore_name}": get_resolver,
            f"resolve_{plural_underscore_name}": list_resolver,
        },
    )


def mutations(model):
    model_name = model.__name__
    underscore_name = inflection.underscore(model_name)

    create_mutation = type(
        f"Create{model_name}Mutation",
        (django_cud_mutations.DjangoCreateMutation,),
        {"Meta": type("Meta", (object,), {"model": model})},
    )

    update_mutation = type(
        f"Update{model_name}Mutation",
        (django_cud_mutations.DjangoUpdateMutation,),
        {"Meta": type("Meta", (object,), {"model": model})},
    )

    delete_mutation = type(
        f"Delete{model_name}Mutation",
        (django_cud_mutations.DjangoDeleteMutation,),
        {"Meta": type("Meta", (object,), {"model": model})},
    )

    return type(
        f"{model_name}Mutation",
        (graphene.ObjectType,),
        {
            f"create_{underscore_name}": create_mutation.Field(),
            f"update_{underscore_name}": update_mutation.Field(),
            f"delete_{underscore_name}": delete_mutation.Field(),
        },
    )


schema = graphene.Schema(
    query=type(
        "Query",
        (*[queries(model) for model in ALL_MODELS],) + (graphene.ObjectType,),
        {"debug": graphene.Field(DjangoDebug, name="_debug")},
    ),
    mutation=type(
        "Mutation",
        (*[mutations(model) for model in ALL_MODELS],) + (graphene.ObjectType,),
        {},
    ),
)
