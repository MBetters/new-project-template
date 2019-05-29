from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(
        # package id
        username = "mbetters",
        channel = "testing",
        stable_branch_pattern = r"v\d+\.\d+\.\d+.*",
        
        # dependencies
        remotes = None,
        build_policy = "outdated",
        upload_dependencies="all",

        # build configurations
        archs = ["x86_64"], # limit to 64-bit only

        # package upload (REMEMBER to set CONAN_PASSWORD environment variable in Travis CI and AppVeyor)
        login_username = "admin", # TODO: Ensure the local_conan_server is using admin/admin123 for user/pass
        upload = "http://localhost:9300" # using local conan_server
    )
    builder.add_common_builds(pure_c=False)
    builder.run()

