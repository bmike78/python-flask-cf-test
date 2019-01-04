# python-flask-cf-test
Python Flask CloudFoundry Test

This is a very simple Flask project to push up to CloudFoundry for testing.


Log into CloudFoundry:
<pre>
server:/home/mike/cloudfoundry/python-flask-cf-test
# cf login -a https://cf.example.com
API endpoint: https://cf.example.com

Email> mike

Password>
Authenticating...
OK

Targeted org org1

Targeted space playground



API endpoint:   https://cf.example.com (API version: 2.107.0)
User:           mike@example.com
Org:            org1
Space:          playground
</pre>

Push to CloudFoundry
<pre>
server:/home/mike/cloudfoundry/python-flask-cf-test
# cf push python-flask-cf-test
Pushing app python-flask-cf-test to org org1 / space playground as mike...
Getting app info...
Updating app with these attributes...
  name:                python-flask-cf-test
  path:                /home/mike/cloudfoundry/python-flask-cf-test
  buildpack:           python
  command:             python flask.py
  disk quota:          1G
  health check type:   port
  instances:           1
  memory:              1G
  stack:               cflinuxfs2
  routes:
    python-flask-cf-test.cf.example.com

Updating app python-flask-cf-test...
Mapping routes...
Comparing local files to remote cache...
Packaging files to upload...
Uploading files...
 694 B / 694 B [=========================================================================================================================================================================] 100.00% 1s

Waiting for API to complete processing files...

Stopping app...

Staging app and tracing logs...
   Downloading dotnet_core_buildpack...
   Downloading java_buildpack_v4...
   Downloading ruby_buildpack...
   Downloading php_buildpack...
   Downloading nodejs_buildpack...
   Downloaded ruby_buildpack
   Downloading go_buildpack...
   Downloaded nodejs_buildpack
   Downloading python_buildpack...
   Downloaded dotnet_core_buildpack
   Downloading java_offline_buildpack...
   Downloaded php_buildpack
   Downloading binary_buildpack...
   Downloaded java_buildpack_v4
   Downloaded python_buildpack
   Downloading staticfile_buildpack...
   Downloaded go_buildpack
   Downloading java_buildpack...
   Downloaded java_offline_buildpack
   Downloaded binary_buildpack
   Downloaded java_buildpack
   Downloaded staticfile_buildpack
   Cell a530023c-395e-4a08-9bf9-a78364bf42a8 creating container for instance 6b8d7f05-5494-4fa5-a4e9-57cd8f48a382
   Cell a530023c-395e-4a08-9bf9-a78364bf42a8 successfully created container for instance 6b8d7f05-5494-4fa5-a4e9-57cd8f48a382
   Downloading app package...
   Downloading build artifacts cache...
   Downloaded app package (694B)
   Downloaded build artifacts cache (37.7M)
   -----> Python Buildpack version 1.6.11
   -----> Supplying Python
   -----> Installing python 2.7.14
          Copy [/tmp/cache/final/dependencies/31ece34385cf05bc471c2efddee7a4a0e147049b19069886d2d6edbbba3e4492/python-2.7.14-linux-x64-30d9c08f.tgz]
   -----> Installing setuptools 38.5.2
          Copy [/tmp/cache/final/dependencies/571e2b3213d04071ad69dc8b7f3b00e26ba3edc6cc084a0d188999b19e55715c/setuptools-38.5.2-8246123e.zip]
   -----> Installing pip 9.0.1
          Copy [/tmp/cache/final/dependencies/e0e373731722cde86f6cdf70813720f534db1557f4dbdfb539031ef7c10dfdfe/pip-9.0.1-35f01da3.tar.gz]
   -----> Installing pip-pop 0.1.1
          Copy [/tmp/cache/final/dependencies/e7f3df1a49d628e69b68a5705ca720d0ecc39e3830867e7128007e03843d921a/pip-pop-0.1.1-d410583a.tar.gz]
   -----> Installing pipenv 11.1.4
          Copy [/tmp/cache/final/dependencies/567e023c14bfa0a7db4d907a05c5f6e91b9d7e420aaf00a93a7199a358c492cf/pipenv-v11.1.4-7394418e.tgz]
   -----> Running Pip Install
          Collecting Flask (from -r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/77/32/e3597cb19ffffe724ad4bf0beca4153419918e7fa4ba6a34b04ee4da3371/Flask-0.12.2-py2.py3-none-any.whl
          Collecting Jinja2>=2.4 (from Flask->-r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
          Collecting Werkzeug>=0.7 (from Flask->-r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl
          Collecting click>=2.0 (from Flask->-r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl
          Collecting itsdangerous>=0.21 (from Flask->-r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz
          Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->Flask->-r /tmp/contents558738512/deps/0/requirements.txt (line 1))
            Using cached https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
          Installing collected packages: MarkupSafe, Jinja2, Werkzeug, click, itsdangerous, Flask
            Running setup.py install for MarkupSafe: started
              Running setup.py install for MarkupSafe: finished with status 'done'
            Running setup.py install for itsdangerous: started
              Running setup.py install for itsdangerous: finished with status 'done'
          Successfully installed Flask-0.12.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24
          You are using pip version 9.0.1, however version 10.0.1 is available.
          You should consider upgrading via the 'pip install --upgrade pip' command.
   Exit status 0
   Uploading droplet, build artifacts cache...
   Uploading build artifacts cache...
   Uploading droplet...
   Uploaded build artifacts cache (37.7M)
   Uploaded droplet (41M)
   Uploading complete
   Cell a530023c-395e-4a08-9bf9-a78364bf42a8 stopping instance 6b8d7f05-5494-4fa5-a4e9-57cd8f48a382
   Cell a530023c-395e-4a08-9bf9-a78364bf42a8 destroying container for instance 6b8d7f05-5494-4fa5-a4e9-57cd8f48a382
   Cell a530023c-395e-4a08-9bf9-a78364bf42a8 successfully destroyed container for instance 6b8d7f05-5494-4fa5-a4e9-57cd8f48a382

Waiting for app to start...

name:              python-flask-cf-test
requested state:   started
instances:         1/1
usage:             1G x 1 instances
routes:            python-flask-cf-test.cf.example.com
last uploaded:     Tue 24 Apr 13:04:18 CDT 2018
stack:             cflinuxfs2
buildpack:         python
start command:     python python-flask-cf-test.py

     state     since                  cpu    memory    disk      details
#0   running   2018-04-24T18:05:23Z   0.0%   0 of 1G   0 of 1G
</pre>

Visit route URL: http://python-flask-cf-test.cf.example.com
