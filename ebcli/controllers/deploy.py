# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from ebcli.core.abstractcontroller import AbstractBaseController
from ebcli.resources.strings import strings
from ebcli.core import operations
from ebcli.objects.exceptions import NoEnvironmentForBranchError, \
    InvalidOptionsError
from ebcli.core import io


class DeployController(AbstractBaseController):
    class Meta(AbstractBaseController.Meta):
        label = 'deploy'
        description = strings['deploy.info']
        arguments = [
            (['environment_name'], dict(action='store', nargs='?',
                                        default=[],
                                        help='Environment name')),
            (['-r', '--region'], dict(help='Region where environment lives')),
            (['--version'], dict(help='Existing version label to deploy')),
            (['-l', '--label'], dict(help='Label to give version')),
            (['-m', '--message'], dict(help='Message/Description for version'))
        ]
        usage = AbstractBaseController.Meta.usage.replace('{cmd}', label)

    def do_command(self):
        app_name = self.get_app_name()
        region = self.get_region()
        env_name = self.app.pargs.environment_name
        version = self.app.pargs.version
        label = self.app.pargs.label
        message = self.app.pargs.message

        if version and (message or label):
            raise InvalidOptionsError(strings['deploy.invalidoptions'])

        if not env_name:
            env_name = \
                operations.get_setting_from_current_branch('environment')

        if not env_name:
            message = strings['branch.noenv'].replace('eb {cmd}',
                                                      self.Meta.label)
            io.log_error(message)
            raise NoEnvironmentForBranchError()

        # ToDo add support for deploying to multiples?
        # for arg in self.app.pargs.environment_name:
        #     # deploy to every environment listed
        #     ## Right now you can only list one

        operations.deploy(app_name, env_name, region, version, label, message)

    def complete_command(self, commands):
        #ToDo, edit this if we ever support multiple env deploys
        super(DeployController, self).complete_command(commands)

        #ToDo, eventually add support for autocompleting
        ## versionlabels on --version