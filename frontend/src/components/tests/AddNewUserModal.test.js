import AddNewUserModal from '@/components/AddNewUserModal';
import { shallowMount } from '@vue/test-utils';
import { createVuetify } from 'vuetify';
import { createStore } from 'vuex';

describe('AddNewUserModal', () => {
    let store;
    let wrapper;
    let vuetify;
    beforeEach(() => {
        vuetify = createVuetify();
        store = createStore({ 
            modules: {
                userLeaderboards: {
                    namespaced: true,
                    actions: {
                        addUser: jest.fn().mockImplementation(() => Promise.resolve()),
                    },
                },
            },
        });
        wrapper = shallowMount(AddNewUserModal, {
            global: {
                plugins: [store, vuetify],
            },
    
            })
            });

    it('renders properly', () => {
        expect(wrapper).toBeTruthy();
        expect(wrapper.vm.name).toBe('');
        expect(wrapper.vm.age).toBe(0);
        expect(wrapper.vm.address).toBe('');
        expect(wrapper.vm.dialog).toBe(false);
        expect(wrapper.vm.isFormValid).toBe(false);
    });

    it('should emit an event when the form is submitted', async () => {
        wrapper.vm.dialog = true;
        wrapper.vm.name = 'test';
        wrapper.vm.age = 20;
        wrapper.vm.address = 'test';
        expect(wrapper.emitted('user-added')).toBeFalsy();
        await wrapper.vm.handleSubmit();
        expect(wrapper.emitted('user-added')).toBeTruthy();
        expect(wrapper.vm.dialog).toBe(false);
        expect(wrapper.vm.name).toBe('');
        expect(wrapper.vm.age).toBe(0);
        expect(wrapper.vm.address).toBe('');
    });
});