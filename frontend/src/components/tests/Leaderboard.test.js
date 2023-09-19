import LeaderBoard from '@/components/LeaderBoard';
import { createLocalVue, mount, shallowMount } from '@vue/test-utils';
import vuetify from 'vuetify';



describe('Leaderboard', () => {
    let wrapper;
    beforeEach(() => {
        const localVue = createLocalVue();
        localVue.use(vuetify);

        wrapper = shallowMount(LeaderBoard, {
            localVue,
        });
    });

    it('renders a vue instance', () => {
        expect(shallowMount(Home).isVueInstance()).toBe(true);
      });
});