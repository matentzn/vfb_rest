from django.apps import AppConfig


from .neo import neo

class VfbidserverConfig(AppConfig):
    name = 'vfb_server'
    verbose_name = "VFB Web Services: Curation"

    def ready(self):
        print("Test")
        #self.loadDatasets()
        #self.loadVFBids()

    def loadDatasets(self):
        from .models import dataset
        kb = neo()
        q = 'MATCH (n:DataSet) RETURN n'
        result = kb.query(q)
        if result:
            for n in result:
                iri = n['n']['iri']
                print(iri)
                ds = dataset(datasetid=iri, datasetlabel='')
                ds.save(force_insert=False)

    def loadVFBids(self):
        from .models import neuron
        kb = neo()
        m_ids = kb.getVFBIds()
        i = 0
        for n in m_ids:
            print(n)
            label = m_ids.get(n)
            n = kb.getNeuronMetadata(n)
            vid = n['vfbid']
            ds = neuron(vfbid=vid, primary_name=label)
            ds.save()
            i = i + 1
            if i>10:
                break