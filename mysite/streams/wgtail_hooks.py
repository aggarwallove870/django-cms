import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core import hooks


@hooks.register("register_rich_text_features")
def register_code_styling(features):
    """Add the <code> to the richtext editor and page."""

    # Step 1
    feature_name = "code"
    type_ = "CODE"
    tag = "code"

    # Step 2
    control = {
        "type": type_,
        "label": "</>",
        "description": "Code"
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: {"element": tag}}}
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6. This is optional
    # This will register this feature with all richtext editors by default
    features.default_features.append(feature_name)


# @hooks.register("register_rich_text_features")
# def register_centertext_feature(features):
#     """Creates centered text in our richtext editor and page."""

#     # Step 1
#     feature_name = "center"
#     type_ = "CENTERTEXT"
#     tag = "div"

#     # Step 2
#     control = {
#         "type": type_,
#         "label": "Center",
#         "description": "Center Text",
#         "style": {
#             "display": "block",
#             "text-align": "center",
#         },
#     }

#     # Step 3
#     features.register_editor_plugin(
#         "draftail", feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     # Step 4
#     db_conversion = {
#         "from_database_format": {tag: InlineStyleElementHandler(type_)},
#         "to_database_format": {
#             "style_map": {
#                 type_: {
#                     "element": tag,
#                     "props": {
#                         "class": "d-block text-center"
#                     }
#                 }
#             }
#         }
#     }

#     # Step 5
#     features.register_converter_rule("contentstate", feature_name, db_conversion)

#     # Step 6, This is optional.
#     features.default_features.append(feature_name)

# import wagtail.admin.rich_text.editors.draftail.features as draftail_features
# from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
# from wagtail.core import hooks

# @hooks.register('register_rich_text_features')
# def register_text_align_left_feature(features):
#     feature_name = 'alignleft'
#     type_ = 'ALIGNLEFT'
#     tag = 'span'

#     # 2. Configure how Draftail handles the feature in its toolbar.
#     control = {
#         'type': type_,
#         'label': 'L',
#         'description': 'Align left',
#         'style': {'textAlign': 'left'},
#     }

#     # 3. Call register_editor_plugin to register the configuration for Draftail.
#     features.register_editor_plugin(
#         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     # 4.configure the content transform from the DB to the editor and back.
#     db_conversion = {
#         'from_database_format': {tag: InlineStyleElementHandler(type_)},
#         'to_database_format': {'style_map': {type_: tag}},
#     }

#     # 5. Call register_converter_rule to register the content transformation conversion.
#     features.register_converter_rule('contentstate', feature_name, db_conversion)

#     features.default_features.append('alignleft')
# @hooks.register('register_rich_text_features')
# def register_text_align_center_feature(features):
#     feature_name = 'aligncenter'
#     type_ = 'ALIGNCENTER'
#     tag = 'span'

# # 2. Configure how Draftail handles the feature in its toolbar.
#     control = {
#         'type': type_,
#         'label': 'C',
#         'description': 'Align center',
#         'style': {'textAlign': 'center'},
#     }

#     # 3. Call register_editor_plugin to register the configuration for Draftail.
#     features.register_editor_plugin(
#         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     # 4.configure the content transform from the DB to the editor and back.
#     db_conversion = {
#         'from_database_format': {tag: InlineStyleElementHandler(type_)},
#         'to_database_format': {'style_map': {type_: tag}},
#     }

#     # 5. Call register_converter_rule to register the content transformation conversion.
#     features.register_converter_rule('contentstate', feature_name, db_conversion)

#     features.default_features.append('aligncenter')