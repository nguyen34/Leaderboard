import LeaderBoard from '@/components/LeaderBoard.vue';
import { expect } from '@jest/globals';
import { shallowMount } from '@vue/test-utils';
import { createVuetify } from 'vuetify';
import { createStore } from 'vuex';

describe('LeaderBoard', () => {
    let store;
    let wrapper;
    let vuetify;
    beforeEach(() => {
        vuetify = createVuetify();
        store = createStore({
            modules: {
                userLeaderboards: {
                    namespaced: true,
                    state: {
                        users: [],
                    },
                    actions: {
                        fetchUsers: jest.fn().mockImplementation(() => Promise.resolve()),
                    },
                },
            },
        });
        wrapper = shallowMount(LeaderBoard, {
            global: {
                plugins: [store, vuetify],
            },
        });
    });

    it('renders properly', () => {
        expect(wrapper).toBeTruthy();
        expect(wrapper.vm.showUserDetails).toBe(false);
        expect(wrapper.vm.selectedUser).toEqual(null);
        expect(wrapper.vm.searchFilter).toBe('');
        expect(wrapper.vm.displayedUsers).toEqual([]);
        expect(wrapper.vm.sortOrder).toBe('desc');
        expect(wrapper.vm.sortHeader).toBe('points');
    });

    });