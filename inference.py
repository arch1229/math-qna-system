import logging

from util.entity_intent_reader import EntityIntentReader
from unit_knowledge.unit_knowledge_list import uk_list
from util.getter.nlg_getter import nlg_getter
from util.setter.nlg_input_setter import nlg_input_setter
from util.nl_printer import nl_printer
from util.result_message_list import QUESTION_NO_INDENT


logger = logging.getLogger("inference_engine.inference")


def inference(question):
    entity_intent = EntityIntentReader(question)
    intent = entity_intent.intent
    result = ""
    inference_result = ""
    try:
        if intent == "action":
            uk = uk_list[entity_intent.action_unit_knowledge["data_en"]]
            inference_result = uk.action(entity_intent.action_unit_knowledge["data_en"], \
                entity_intent.action_expression_list)

        elif intent == "component":
            uk = uk_list[entity_intent.component_unit_knowledge["data_en"]]
            inference_result = uk.component(entity_intent.component_unit_knowledge["data"], \
                entity_intent.component)

        elif intent == "logic":
            uk = uk_list[entity_intent.logic_unit_knowledge["data_en"]]
            inference_result = uk.logic(entity_intent.logic_expression)

        elif intent == "implication":
            uk = uk_list[entity_intent.implication_unit_knowledge_master["data_en"]]
            inference_result = uk.implication(entity_intent.implication_unit_knowledge_master["data"], \
                entity_intent.implication_unit_knowledge_slave["data"])

        else:
            logger.info("Undefined query type entered.")
            inference_result = QUESTION_NO_INDENT

        nlg_input = nlg_input_setter(question, inference_result)
        logger.debug("----nlg_input------")
        logger.debug(nlg_input)
        
        nlg_output = nlg_getter(nlg_input)
        logger.debug("----nlg_output-----")
        logger.debug(nlg_output)
        
        result = nl_printer(nlg_output)
        
    except Exception as e:
        logger.debug(e)
        result = e

    logger.debug("----inference_input----")
    logger.debug(entity_intent.entity)
    logger.debug("----inference_result----")
    logger.debug(inference_result)

    return result