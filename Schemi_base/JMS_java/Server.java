package JMS_java;

import java.util.Hashtable;
import javax.jms.*;
import javax.naming.*;

public class Server{

    /**
     * @param args
     */
    public static void main(String[] args) {
        Hashtable<String,String> prop = new Hashtable<String,String>();
        prop.put("idk","idk");
        prop.put("idk2","idk2");

        prop.put("queue.test1", "mytest1");
        prop.put("queue.test2", "mytest2");

        try {
            
            Context jndiContext = new InitialContext(prop);
            QueueConnectionFactory connFactory = (QueueConnectionFactory) jndiContext.lookup("QueueConnectionFactory");
            Queue queue  = (Queue) jndiContext.lookup("test1");
            Queue queue2 = (Queue)jndiContext.lookup("test2");

            QueueConnection qConnection = connFactory.createQueueConnection();
            qConnection.start();
            QueueSession qSession = qConnection.createQueueSession(false, 0);
            QueueReceiver rec = qSession.createReceiver(queue);
            MsgListener listener = new MsgListener(qConnection, queue2);
            rec.setMessageListener(listener);
            
            while (true) {
                Thread.sleep(6000);
            }

        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
}
