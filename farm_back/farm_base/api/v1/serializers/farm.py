from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from farm_base.api.v1.serializers.owner import OwnerDetailSerializer
from farm_base.models import Farm, Owner


class FarmListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(FarmListSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include_geometry = request.GET.get('include_geometry', "false")

        if include_geometry.lower() == "true":
            self.fields['geometry'] = GeometryField(read_only=True)

    class Meta:
        model = Farm

        #All visible fields of Farm added in the List Serializer, including the owner's id.
        fields = ['name', 'owner', 'centroid', 'area', 'municipality', 'state']
        read_only_fields = ['id', 'centroid', 'area']



class FarmCreateSerializer(serializers.ModelSerializer):
    def validate_geometry(self, data):
        if data.hasz:
            g = ogr.CreateGeometryFromWkt(data.wkt)
            g.Set3D(False)
            data = GEOSGeometry(g.ExportToWkt())
        return data

    class Meta:
        model = Farm
        #Added municipality, state and owner into the Serializer's Create.
        fields = ['id', 'owner', 'name', 'geometry', 'is_active', 'municipality', 'state', 'centroid', 'area']
        read_only_fields = ['id', 'centroid', 'area']

    #Created a validator for Owner, so it won't be set as Null when creating a Farm.
    def validate(self, data):
        if data['owner'] == None:
            raise serializers.ValidationError("Owner can't be Null.")
        return data

class FarmDetailSerializer(serializers.ModelSerializer):
    owner = OwnerDetailSerializer(read_only=True)

    class Meta:
        model = Farm
        #All fields of Farm added into the DetailSerializer.
        fields = '__all__'
        read_only_fields = ['id', 'centroid', 'area']
