from rest_framework import serializers
from inmuebleslist_app.models import Inmueble, Empresa, Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    
    comentario_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comentario
        exclude = ['inmueble']
        #fields = "__all__"

class InmuebleSerializer(serializers.ModelSerializer):
    
    comentarios = ComentarioSerializer(many=True, read_only=True)
    
    class Meta:
        model = Inmueble
        fields = "__all__"
        #fields = ['id', 'descripcion', 'imagen'] 
        #exclude = ['id']

class EmpresaSerializer(serializers.ModelSerializer):
    
    inmuebleList = InmuebleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Empresa
        fields = "__all__"
        
    #inmueble_list = InmuebleSerializer(many=True, read_only=True)
    #inmueble_list = serializers.StringRelatedField(many=True)
    #inmueble_list = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='inmueble_detail')
    #Llama al metodo str del models

        
    # def get_longitud_direccion(self, object):
    #     cant_caract = len(object.direccion)
    #     return cant_caract
        
    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("La direccion y el pais deben ser diferentes")
    #     else:
    #         return data
        
    # def validate_imagen(self, data):
    #     if len(data) < 8:
    #         raise serializers.ValidationError("La url de la imagen es muy corta")
    #     else:
    #         return data
        

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es demasiado corto")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    