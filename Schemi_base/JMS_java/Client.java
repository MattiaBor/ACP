package JMS_java;

import java.util.Hashtable;
import javax.jms.*;
import javax.naming.*;

public class Client{

    public static void main(String[] args) {
        
        Hashtable<String,String> prop = new Hashtable<String,String>();
        prop.put("idk","idk");
        prop.put("idk2","idk2");

        prop.put("queue.test1", "mytest1");
        prop.put("queue.test2", "mytest2");

        try {
            
            Context jndiContext = new InitialContext(prop);
            QueueConnectionFactory connFactory = (QueueConnectionFactory) jndiContext.lookup("QueueConnectionFactory");
            Queue queue= (Queue) jndiContext.lookup("test");

            QueueConnection qConnection = connFactory.createQueueConnection();
            QueueSession qSession = qConnection.createQueueSession(false, 0);
            QueueSender sender = qSession.createSender(queue);

            TextMessage text = qSession.createTextMessage();
            
            for (int i = 0; i < 10; i++) {
                String msg = "prova";
                Integer c = i;
                text.setText(String.join(msg,c.toString()));
                sender.send(text);
            }

            sender.close();
            qSession.close();
            qConnection.close();

        } catch (Exception e) {
            e.setStackTrace(null);
        }

    }

}