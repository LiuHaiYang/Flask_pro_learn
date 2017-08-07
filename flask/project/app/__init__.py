from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
api = Api()
db = MongoEngine()
def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'host': '202.206.168.139',
        'port': 27017,
        'db': 'rec'}
    db.init_app(app)
    api.init_app(app)
    return app


# class DataAPI(Resource):
#     def get(self,srouse,start,end):
#         if srouse == 'target_rec':
#             l = []
#             tar_info = target_rec.objects.all()
#             for tar in tar_info:
#                 l.append(tar)
#             return jsonify({"target_rec":l})
#         elif srouse == 'pins_rec':
#             p = []
#             pins_info = pins_rec.objects.all()
#             for pin_i in pins_info:
#                 p.append(pin_i)
#             return  jsonify({"pins_rec":p})
#         else:
#             pass
# api.add_resource(DataAPI, '/api/1.0/<string:srouse>/<string:start>/<string:end>')
#
# class FxAPI(Resource):
#     def post(self):
#         data = pd.DataFrame(request.json)
#         data_1 = data[data['Target_Signal'] > 0]
#         fenxi = data_1.groupy([data_1['Target_ID'],data_1['Pin_ID']]).size()
#         fenxi_1 = fenxi.unstack().T.fillna(value= 0)
#         return  fenxi_1.tojson()
# api.add_resource(FxAPI, '/v1.0/data/trace')



# if __name__ == '__main__':
#     app.run(debug=True)
