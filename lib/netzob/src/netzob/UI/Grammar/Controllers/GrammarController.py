# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
from gettext import gettext as _
import logging
from netzob.Inference.Grammar.AutomaticGrammarInferenceView import AutomaticGrammarInferenceView
from netzob.UI.Grammar.Views.GrammarView import GrammarView
from netzob.UI.Grammar.Controllers.CreateStateController import CreateStateController
from netzob.UI.Grammar.Controllers.CreateSemiStochasticTransitionController import CreateSemiStochasticTransitionController
from netzob.UI.Grammar.Controllers.CreateOpenChannelTransitionController import CreateOpenChannelTransitionController
from netzob.UI.Grammar.Controllers.CreateCloseChannelTransitionController import CreateCloseChannelTransitionController


#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+


#+---------------------------------------------------------------------------+
#| GrammarInferenceController:
#|    Graphical display of the inferring process of a grammar
#+---------------------------------------------------------------------------+
class GrammarController(object):

    def __init__(self, netzob):
        self.netzob = netzob
        self._view = GrammarView(self)
        self.log = logging.getLogger(__name__)

    @property
    def view(self):
        return self._view

    def restart(self):
        """Restart the view"""
        logging.debug("Restarting the grammar perspective")
        self._view.restart()

    def activate(self):
        """Activate the perspective"""
        self.restart()

    def deactivate(self):
        pass

    def getCurrentProject(self):
        """Return the current project (can be None)"""
        return self.netzob.getCurrentProject()

    def getCurrentWorkspace(self):
        """Return the current workspace"""
        return self.netzob.getCurrentWorkspace()

    def activeGrammarInferring_activate_cb(self, event):
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

        agi = AutomaticGrammarInferenceView(self.getCurrentProject())
        agi.display()

    def passiveGrammarInferring_activate_cb(self, event):
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

    def createState_activate_cb(self, event):
        """Callback executed when the user wants
        to create a state"""
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

        createStateController = CreateStateController(self)
        createStateController.run()

    def createSemiStochasticTransition_activate_cb(self, event):
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

        createTransitionController = CreateSemiStochasticTransitionController(self, None)
        createTransitionController.run()

    def createOpenChannelTransition_activate_cb(self, event):
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

        createTransitionController = CreateOpenChannelTransitionController(self, None)
        createTransitionController.run()

    def createCloseChannelTransition_activate_cb(self, event):
        if self.getCurrentProject() is None:
            logging.info("No project loaded.")
            return

        createTransitionController = CreateCloseChannelTransitionController(self, None)
        createTransitionController.run()
