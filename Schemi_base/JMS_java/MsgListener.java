package JMS_java;

import javax.jms.*;

public class MsgListener implements MessageListener {
    
    private QueueConnection conn;
    private Queue queue;

    public MsgListener(QueueConnection conn, Queue queue){
        this.conn=conn;
        this.queue=queue;
    }

    @Override
    public void onMessage(Message arg0) {
        
        try {
            QueueSession qSession = conn.createQueueSession(false, 0);
            QueueSender sender = qSession.createSender(queue);

            TextMessage text = qSession.createTextMessage();
            
            text.setText(String.join("ack -",arg0.toString()));
            sender.send(text);
            
            sender.close();
            qSession.close();
        } catch (Exception e) {
            // TODO: handle exception
        }

    }
}
