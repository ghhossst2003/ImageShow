// const host = 'http://192.168.1.136:5000/'
const host = 'http://127.0.0.1:5000/'

const config = {
    imageServer: `${host}`,
    url: {
        getAllWorks: `${host}/works`,//works
        getWorksForPage: `${host}/works_page/`,
        login: `${host}/login`
    }
}
export default config
