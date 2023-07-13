//

module.exports = (grunt) => {
    grunt.loadNpmTasks('grunt-crx')
    // grunt.loadNpmTasks('grunt-contrib-copy')
    grunt.initConfig({
        crx: {
            myPublicExtension: {
                src: "extensions/**/*",
                dest: "dist/TwitterBlocker.zip"
            },
            mySignedExtension: {
                src: "extensions/**/*",
                dest: "dist/TwitterBlocker.crx",
                options: {
                    privateKey: "dist/key.pem"
                }
            }
        }
    })

    grunt.registerTask('crxTask', ['crx'])
}