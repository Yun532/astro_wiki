// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://yun532.github.io',
	base: '/astro_wiki',
	integrations: [
		starlight({
			title: '高能天体物理中文知识库',
			sidebar: [
				{ label: '总览', items: [{ autogenerate: { directory: '00_总览' } }] },
				{ label: '理论', items: [{ autogenerate: { directory: '10_理论' } }] },
				{ label: '理论课程', items: [{ autogenerate: { directory: 'textbook' } }] },
				{ label: '天体源', items: [{ autogenerate: { directory: '20_天体源' } }] },
				{ label: '仪器', items: [{ autogenerate: { directory: '30_仪器' } }] },
				{ label: '综合比较', items: [{ autogenerate: { directory: '40_综合比较' } }] },
				{ label: '模型', items: [{ autogenerate: { directory: '50_模型' } }] },
				{ label: '元信息', items: [{ autogenerate: { directory: '90_元信息' } }] },
				{ label: '知识星图', items: [{ label: '交互图谱', link: '/graph/' }] },
			],
		}),
	],
});
