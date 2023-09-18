import { createLocalVue, shallowMount } from '@vue/test-utils';
import Vuetify from 'vuetify';
import Vue from 'vue';
import Vuex from 'vuex';
import AddNewUserModal from '@/components/AddNewUserModal.vue';

Vue.use(Vuex);
Vue.use(Vuetify);

describe('AddNewUserModal.vue', () => {
    let wrapper;
    let actions;
    let store;
    let vuetify;
    
    beforeEach(() => {
        vuetify = new Vuetify();
        actions = {
        addUser: jest.fn(),
        };
        store = new Vuex.Store({
        actions,
        });
        wrapper = shallowMount(AddNewUserModal, {
        store,
        localVue: createLocalVue(),
        vuetify,
        });
    });
    
    it('should call addUser action when save button is clicked', () => {
        wrapper.find('[data-testid="save"]').trigger('click');
        expect(actions.addUser).toHaveBeenCalled();
    });
    });