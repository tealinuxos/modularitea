export default [
  {
    path: '/',
    name: 'landing-page',
    component: require('components/Modularitea')
  },
  {
    path: '/module/:folderName',
    name: 'module-detail',
    component: require('components/Modularitea/ModuleDetail')
  },
  {
    path: '*',
    redirect: '/'
  }
]
