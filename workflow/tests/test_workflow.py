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
            'description': 'Test Description',
            'link': 'https://www.example.com',
        })

    def test_01_workflow_values(self):
        workflow_id = self.workflow_01_record

        self.assertEqual(workflow_id.partner_id.ids, [self.env.ref('base.user_admin').id])

        self.assertRecordValues(workflow_id, [{
            'indicator_number': 1,
            'sequence': 1,
            'summary': 'Test Summary',
            'verification_status': 'not_verified',
            'description': 'Test Description',
            'link': 'https://www.example.com',
        }])

        
        _logger.info('TestWorkflow.test_01_workflow_values executed successfully')

    def test_02_toggle_verification(self):
        workflow_id = self.workflow_01_record
        

        workflow_id.toggle_verification()
        self.assertEqual(workflow_id.verification_status, 'verified')
        self.assertIn("The record has been verified.", workflow_id.message_ids.mapped('body'))


        workflow_id.toggle_verification()
        self.assertEqual(workflow_id.verification_status, 'not_verified')
        self.assertIn("The record is not verified.", workflow_id.message_ids.mapped('body'))

        _logger.info('TestWorkflow.test_02_toggle_verification executed successfully')

    def test_03_verify_link(self):
        workflow_id = self.workflow_01_record
        
   
        action = workflow_id.verify_link()
        self.assertEqual(action['type'], 'ir.actions.client')
        self.assertEqual(action['tag'], 'display_notification')
        self.assertEqual(action['params']['title'], 'Success!')
        self.assertEqual(action['params']['message'], 'The link exists.')


        workflow_id.link = 'https://www.invalid-link.com'
        action = workflow_id.verify_link()
        self.assertEqual(action['params']['title'], 'Error!')
        self.assertIn('The link does not exist.', action['params']['message'])

        _logger.info('TestWorkflow.test_03_verify_link executed successfully')