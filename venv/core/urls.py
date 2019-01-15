from django.conf.urls import url, include
from .views import (
    home, pessoas, veiculos, 
    movRotativo, mensalista, movMensalista, 
    nova_pessoa, novo_veiculo, novo_movRotativo,
    novo_mensalista, novo_movMensalista, update_pessoa,
    update_veiculo, update_mensalista, update_movRotativo,
    update_movMensalista, delete_pessoa, delete_veiculo)

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', pessoas, name='core_listaPessoas'),
    url(r'^nova_pessoa/$', nova_pessoa, name='core_novaPessoa'),
    url(r'^update_pessoa/(?P<id>\d+)/$', update_pessoa, name='core_updatePessoa'),
    url(r'^delete_pessoa/(?P<id>\d+)/$', delete_pessoa, name='core_deletePessoa'),

    url(r'^veiculos/$', veiculos, name='core_listaVeiculos'),
    url(r'^update_veiculo/(?P<id>\d+)/$', update_veiculo, name='core_updateVeiculo'),
    url(r'^delete_veiculo/(?P<id>\d+)/$', delete_veiculo, name='core_deleteVeiculo'),
    url(r'^novo_veiculo/$', novo_veiculo, name='core_novoVeiculo'),
    
    url(r'^movRotativo/$', movRotativo , name='core_listaMovRotativo'),
    url(r'^update_movRotativo/(?P<id>\d+)/$', update_movRotativo, name='core_updateMovRotativo'),
    url(r'^novo_movRotativo/$', novo_movRotativo , name='core_novoMovRotativo'),

    
    url(r'^mensalista/$', mensalista , name='core_listaMensalista'),
    url(r'^update_mensalista/(?P<id>\d+)/$', update_mensalista, name='core_updateMensalista'),
    url(r'^novo_mensalista/$', novo_mensalista , name='core_novoMensalista'),
    
    url(r'^movMensalista/$', movMensalista , name='core_listaMovMensalista'),
    url(r'^update_movMensalista/(?P<id>\d+)/$', update_movMensalista, name='core_updateMovMensalista'),
    url(r'^novo_movMensalista/$', novo_movMensalista , name='core_novoMovMensalista')
]