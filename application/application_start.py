from flask import Blueprint, request
from dao import parts_dao, factory_dao, factory_part_mapping_dao

parts = Blueprint("parts", __name__, template_folder="templates")
factory = Blueprint("factory", __name__, template_folder="templates")

@factory.route('/get_all_factory_info', methods=['GET'])
def getAllFactoryInfo():
    return factory_dao.get_all_factory()

@factory.route('/get_nearest_factory/<longitude>/<latitude>', methods=['GET'])
def getNearestFactory(longitude, latitude):
    return factory_dao.get_nearest_factory(longitude, latitude)

@factory.route('/get_factory_info/<factoryId>', methods=['GET'])
def getFactoryInfo(factoryId):
    return factory_dao.read_factory(factoryId)

@factory.route('/create_factory', methods=['POST'])
def createPart():
    return factory_dao.create_factory(request.json.get('name'), request.json.get('longitude'), request.json.get('latitude'))

@factory.route('/update_factory_info', methods=['POST'])
def updateFactoryInfo():
    return factory_dao.update_factory(request.json.get('factoryId'), request.json.get('name'), request.json.get('longitude'), request.json.get('latitude'))

@factory.route('/get_factory_part/<factoryId>', methods=['GET'])
def getFactoryPartByFactoryId(factoryId):
    return factory_part_mapping_dao.get_all_factory_parts(factoryId)

@factory.route('/get_factory_part/<factoryId>/<partId>', methods=['GET'])
def getFactoryPartByFactoryIdAndPartId(factoryId, partId):
    return factory_part_mapping_dao.get_factory_part(factoryId, partId)

@factory.route('/update_factory_part', methods=['POST'])
def updateFactoryPart():
    mapping = factory_part_mapping_dao.get_factory_part(request.json.get('factoryId'), request.json.get('partId'))
    if mapping:
        return factory_part_mapping_dao.update_factory_part(request.json.get('factoryId'), request.json.get('partId'), request.json.get('quantity'))
    else:
        return factory_part_mapping_dao.create_factory_part(request.json.get('factoryId'), request.json.get('partId'), request.json.get('quantity'))

@parts.route('/get_all_parts_info', methods=['GET'])
def getAllPartsInfo():
    return parts_dao.get_all_part()

@parts.route('/get_parts_info/<partId>', methods=['GET'])
def getPartInfo(partId):
    return parts_dao.read_part(partId)

@parts.route('/update_part_info', methods=['POST'])
def updatePartInfo():
    return parts_dao.update_part(request.json.get('partId'), request.json.get('name'))

@parts.route('/delete_part', methods=['POST'])
def deletePart():
    return parts_dao.delete_part(request.json.get('partId'))

@parts.route('/reactive_part', methods=['POST'])
def reactivePart():
    return parts_dao.reactive_part(request.json.get('partId'))

@parts.route('/create_part', methods=['POST'])
def createPart():
    return parts_dao.create_part(request.json.get('name'))