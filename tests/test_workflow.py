import logging
from odoo.tests.common import TransactionCase
from odoo import fields

_logger = logging.getLogger(__name__)

class TestWorkflow(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp()

        self.workflow_01_record = self.env['workflow'].create({
            'indicator_number': 1,
            'sequence': 1,
            'summary': 'Test Summary',
            'partner_id': [(6, 0, [self.env.ref('base.user_admin').id])],
            'verification_status': 'not_verified',
<<<<<<< HEAD
=======
            'verification_date': fields.Date.today(),
            'verified_by': self.env.ref('base.user_admin').id,
>>>>>>> origin2/ithar-workflow
            'description': 'Test Description',
            'link': 'https://www.example.com',
        })

    def test_01_workflow_values(self):
        workflow_id = self.workflow_01_record

<<<<<<< HEAD
        self.assertEqual(workflow_id.partner_id.ids, [self.env.ref('base.user_admin').id])

=======
        # Check partner_id separately
        self.assertEqual(workflow_id.partner_id.ids, [self.env.ref('base.user_admin').id])

        # Check the other fields
>>>>>>> origin2/ithar-workflow
        self.assertRecordValues(workflow_id, [{
            'indicator_number': 1,
            'sequence': 1,
            'summary': 'Test Summary',
            'verification_status': 'not_verified',
<<<<<<< HEAD
=======
            'verification_date': fields.Date.today(),
            'verified_by': self.env.ref('base.user_admin').id,
>>>>>>> origin2/ithar-workflow
            'description': 'Test Description',
            'link': 'https://www.example.com',
        }])

        
<<<<<<< HEAD
        _logger.info('TestWorkflow.test_01_workflow_values executed successfully')
=======
        _logger.info('TestWorkflow.test_01_workflow_values executed successfully')
>>>>>>> origin2/ithar-workflow
