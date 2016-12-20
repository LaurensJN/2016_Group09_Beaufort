    import * from utility_testing
    
    
    def calculateAllRoutes(self):
        incidents = self.getAllIncidents()
        layer = uf.getLegendLayerByName(self.iface, "brandweerautos")
        self.updateAttribute.emit("sid")
        car = self.tied_points

        for incident in incidents:
            attributes = ['id']
            duo = [incident,car]
            #voeg selected brandweerauto en id aan lijst toe
            types = [QtCore.QVariant.String]
            templayer = uf.createTempLayer('temp','POINT',self.network_layer.crs().postgisSrid(),attributes,types)
            uf.insertTempFeatures(templayer, duo)
            self.calculateRoute()